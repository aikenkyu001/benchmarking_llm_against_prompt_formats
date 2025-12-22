import os
import sys
import requests
import json
import re
import subprocess
import time
import argparse
from datetime import datetime
from typing import Optional, Tuple

# --- Configuration ---
OLLAMA_API_URL = None
MAX_RETRIES = 1 # CoT has self-consistency, others are single-shot for now.

# --- File Paths ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AGI_DISTANT_BEYOND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))
TEST_DEFINITION_FILE = os.path.join(AGI_DISTANT_BEYOND_DIR, '06_TestDefinitions', 'test_einstein_riddle.py')

# --- S-Expression Meta-Prompt ---
META_PROMPT_TEMPLATE = """You are a world-class logical reasoner. Your sole task is to solve the logic puzzle defined in the S-expression below.

**CRITICAL INSTRUCTIONS:**
- You MUST perform all reasoning internally.
- Your output MUST be ONLY a single Python code block.
- The Python script MUST contain one function, `solve_puzzle()`.
- The `solve_puzzle()` function, when executed, MUST print the single-word answer to the QUERY.
- The function must `print()` the final answer to standard output, it must NOT `return` a value.
- DO NOT include any explanation, commentary, or natural language text in your response.
- DO NOT print the answer directly in your response. The answer must be printed by the `solve_puzzle()` function.

**EXAMPLE OUTPUT FORMAT:**

```python
def solve_puzzle():
    print("German")
```

Now, solve the following puzzle and provide the output in the format specified above.

**PUZZLE DEFINITION:**
---
{puzzle_content}
---
"""

def query_ollama(prompt: str, model_name: str, temperature: float = 0.0) -> Optional[str]:
    """Sends a prompt to the Ollama API and returns the response."""
    print(f"### Querying Model: `{model_name}` (temperature={temperature})")
    try:
        response = requests.post(
            OLLAMA_API_URL,
            json={'model': model_name, 'prompt': prompt, 'stream': False, 'options': {'temperature': temperature}},
            timeout=120 # Increased timeout for complex reasoning
        )
        response.raise_for_status()
        llm_response = response.json().get('response', '').strip()
        print(f"#### Raw LLM Response (first 100 chars):\n```\n{llm_response[:100]}...\n```")
        return llm_response
    except requests.exceptions.RequestException as e:
        print(f"**ERROR:** API request failed: {e}")
        return None

def extract_python_code(llm_response: str) -> Optional[str]:
    """
    Parses the LLM response to extract the Python code including imports and the solve_puzzle function.
    It looks for a Python markdown block and extracts its entire content.
    """
    print("### Parsing LLM Response for Python code block")
    
    # Find the first python markdown block
    match = re.search(r"```python\s*(.*?)\s*```", llm_response, re.DOTALL)
    if match:
        code = match.group(1).strip()
        # Verify that the extracted code contains the required function
        if "def solve_puzzle" in code:
            print("**INFO:** Successfully extracted Python code block containing 'solve_puzzle()'.")
            return code
        else:
            print("**ERROR:** Python code block found, but it does not contain 'def solve_puzzle()'.")
            return None
    
    print("**ERROR:** Could not find a Python markdown code block in the LLM response.")
    return None

def run_pytest(output_dir: str) -> Tuple[bool, str]:
    """Runs pytest on the generated code and the static test definition."""
    print("### Running Pytest Validation")
    try:
        static_test_content = open(TEST_DEFINITION_FILE, 'r', encoding='utf-8').read()
        with open(os.path.join(output_dir, 'test_einstein_riddle.py'), 'w', encoding='utf-8') as f:
            f.write(static_test_content)
    except IOError as e:
        print(f"**ERROR:** Could not copy test definition file: {e}")
        return False, str(e)

    # Add the directory to pythonpath to ensure imports work
    env = os.environ.copy()
    pythonpath = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = f"{output_dir}{os.pathsep}{pythonpath}"

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest"],
            capture_output=True, text=True, cwd=output_dir, env=env, timeout=60
        )
        output = (result.stdout + '\n' + result.stderr).strip()
        if result.returncode == 0:
            print(f"**Pytest Result: SUCCESS**\n```\n{output}\n```")
            return True, output
        else:
            print(f"**Pytest Result: FAILED**\n```\n{output}\n```")
            return False, output
    except subprocess.TimeoutExpired:
        output = "Pytest execution timed out after 60 seconds."
        print(f"**Pytest Result: FAILED (Timeout)**\n```\n{output}\n```")
        return False, output

def main():
    """Orchestrates the Einstein Riddle logic puzzle test."""
    parser = argparse.ArgumentParser(description="Run the Einstein Riddle logic puzzle test for a given model.")
    parser.add_argument("--output-dir", required=True, help="Directory to save generated files.")
    parser.add_argument("--ollama-url", default=os.getenv('OLLAMA_API_URL'), help="Ollama API URL.")
    parser.add_argument("-m", "--model", default='gemma:2b', help="The name of the Ollama model to test.")
    parser.add_argument("--test-type", choices=['s_expr', 'token_test', 'cot_baseline', 'json'], default='s_expr', help="The type of prompt format to use.")
    parser.add_argument("--lang", default='en', choices=['en', 'ja', 'eo', 'jbo'], help="Language for the CoT prompt (default: en).")
    
    args = parser.parse_args()
    
    global OLLAMA_API_URL
    OLLAMA_API_URL = args.ollama_url
    if OLLAMA_API_URL and not OLLAMA_API_URL.endswith(('/api/generate', '/api/chat')):
        OLLAMA_API_URL = OLLAMA_API_URL.rstrip('/') + '/api/generate'
    
    if OLLAMA_API_URL is None:
        sys.exit("Error: Ollama API URL must be provided via --ollama-url or OLLAMA_API_URL environment variable.")

    os.makedirs(args.output_dir, exist_ok=True)
    solution_path = os.path.join(args.output_dir, 'einstein_solution.py')

    print(f"# Einstein Riddle Logic Test Log for {args.model}\n\n**Date:** {datetime.now().isoformat()}\n**Test Type:** {args.test_type}\n")
    if args.test_type == 'cot_baseline':
        print(f"**Language:** {args.lang}\n")

    # --- Determine Prompt File and Strategy ---
    prompt_file_path = None
    use_meta_prompt = False

    if args.test_type == 's_expr':
        prompt_file_path = os.path.join(AGI_DISTANT_BEYOND_DIR, '04_Prompts', 'prompt_einstein_riddle.sxp')
        use_meta_prompt = True
    elif args.test_type == 'token_test':
        prompt_file_path = os.path.join(AGI_DISTANT_BEYOND_DIR, '04_Prompts', 'prompt_einstein_riddle_token_test.txt')
    elif args.test_type == 'cot_baseline':
        prompt_file_path = os.path.join(AGI_DISTANT_BEYOND_DIR, '04_Prompts', args.lang, f'prompt_einstein_riddle_cot_{args.lang}.md')
    elif args.test_type == 'json':
        prompt_file_path = os.path.join(AGI_DISTANT_BEYOND_DIR, '04_Prompts', 'prompt_einstein_riddle_json.md')
    
    if not prompt_file_path:
        sys.exit(f"**FATAL ERROR:** Could not determine prompt file for test type '{args.test_type}'.")

    try:
        with open(prompt_file_path, 'r', encoding='utf-8') as f:
            puzzle_content = f.read()
    except FileNotFoundError:
        print(f"**FATAL ERROR:** Prompt file not found: {prompt_file_path}")
        sys.exit(1)

    # --- Construct Final Prompt ---
    if use_meta_prompt:
        full_prompt = META_PROMPT_TEMPLATE.format(puzzle_content=puzzle_content)
    else:
        full_prompt = puzzle_content # The entire prompt is in the file

    # --- Execute Test ---
    llm_response = query_ollama(full_prompt, args.model, temperature=0.0)
    if not llm_response:
        sys.exit("**Overall Result: ❌ FAILURE (Query failed)**")

    final_code = extract_python_code(llm_response)
    if not final_code:
        sys.exit("**Overall Result: ❌ FAILURE (Code extraction failed)**")

    try:
        with open(solution_path, 'w', encoding='utf-8') as f:
            f.write(final_code)
        print(f"Content for final `{os.path.basename(solution_path)}` saved.")
    except IOError as e:
        sys.exit(f"**Overall Result: ❌ FAILURE (Failed to write solution file: {e})")

    passed, pytest_output = run_pytest(args.output_dir)
    
    if passed:
        print(f"**Overall Result for `{args.model}`: 🎉 SUCCESS**")
        sys.exit(0)
    else:
        print(f"**Overall Result for `{args.model}`: ❌ FAILURE**")
        sys.exit(1)

if __name__ == "__main__":
    main()