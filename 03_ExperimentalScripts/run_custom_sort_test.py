import argparse
import os
import sys
import requests
import json
import re
import subprocess
from datetime import datetime
from typing import Optional, Tuple

# --- Configuration ---
OLLAMA_API_URL = None
DEFAULT_MODEL_NAME = 'tinyllama:latest'
TIMEOUT = 60

# --- File Paths ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AGI_DISTANT_BEYOND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))
TEST_DEFINITION_FILE = os.path.join(AGI_DISTANT_BEYOND_DIR, '06_TestDefinitions', 'test_custom_sort.py')

def query_ollama(prompt: str, model_name: str) -> Optional[str]:
    """Sends a prompt to the Ollama API and returns the response."""
    print(f"### Querying Model: `{model_name}`")
    try:
        response = requests.post(
            OLLAMA_API_URL,
            json={'model': model_name, 'prompt': prompt, 'stream': False, 'options': {'temperature': 0.0}},
            timeout=TIMEOUT
        )
        response.raise_for_status()
        llm_response = response.json().get('response', '').strip()
        print(f"#### Raw LLM Response (first 300 chars):\n```\n{llm_response[:300]}...\n```")
        return llm_response
    except requests.exceptions.RequestException as e:
        print(f"**ERROR:** API request failed: {e}", file=sys.stderr)
        return None

def extract_python_code(llm_response: str) -> Optional[str]:
    """Parses the LLM response to extract the Python code for the function."""
    print("### Parsing LLM Response for custom_sort() function")
    # Improved regex: makes 'python' optional and handles trailing whitespace better.
    code_blocks = re.findall(r"```(?:python)?\s*(.*?)\s*```", llm_response, re.DOTALL)
    if code_blocks:
        # If there are multiple code blocks, assume the first one is the main one
        return code_blocks[0].strip()
    
    # Fallback if no markdown block is found, look for function definition
    # Fixed the unbalanced parenthesis in the regex
    match = re.search(r"def custom_sort\s*\((.|\n)*", llm_response)
    if match:
        return match.group(0).strip()
        
    print("**ERROR:** Could not find a Python code block or 'def custom_sort(...)' in the LLM response.")
    return None

def run_pytest(output_dir: str) -> Tuple[bool, str]:
    """Runs pytest on the generated code and the static test definition."""
    print("### Running Pytest Validation")
    test_file_in_output = os.path.join(output_dir, 'test_custom_sort.py')
    try:
        # Copy the test definition file to the output directory for execution
        with open(TEST_DEFINITION_FILE, 'r', encoding='utf-8') as src:
            with open(test_file_in_output, 'w', encoding='utf-8') as dest:
                dest.write(src.read())
    except IOError as e:
        print(f"**ERROR:** Could not copy test definition file: {e}")
        return False, str(e)

    env = os.environ.copy()
    pythonpath = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = f"{output_dir}{os.pathsep}{pythonpath}"

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "test_custom_sort.py"],
            capture_output=True, text=True, cwd=output_dir, env=env, timeout=60 # Pass env
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
    """Orchestrates the custom sort code generation test."""
    parser = argparse.ArgumentParser(description="Run the custom sort code generation test for a given model and prompt.")
    parser.add_argument("--output-dir", required=True, help="Directory to save generated files.")
    parser.add_argument("--ollama-url", default=os.getenv('OLLAMA_API_URL'), help="Ollama API URL.")
    parser.add_argument("-m", "--model", default=DEFAULT_MODEL_NAME, help=f"The LLM model to use (default: {DEFAULT_MODEL_NAME})")
    parser.add_argument("--lang", required=True, help="Language of the prompt.")
    args = parser.parse_args()

    global OLLAMA_API_URL
    OLLAMA_API_URL = args.ollama_url
    if OLLAMA_API_URL and not OLLAMA_API_URL.endswith(('/api/generate', '/api/chat')):
        OLLAMA_API_URL = OLLAMA_API_URL.rstrip('/') + '/api/generate'
    
    if OLLAMA_API_URL is None:
        sys.exit("Error: Ollama API URL must be provided via --ollama-url or OLLAMA_API_URL environment variable.")

    os.makedirs(args.output_dir, exist_ok=True)
    solution_path = os.path.join(args.output_dir, 'custom_sort_solution.py')

    # Print log content to stdout, to be redirected by the shell script
    print(f"# Custom Sort Test Log for {args.model}\n\n**Date:** {datetime.now().isoformat()}")
    print(f"**Lang:** {args.lang}\n\n")

    prompt_file_path = os.path.join(AGI_DISTANT_BEYOND_DIR, '04_Prompts', args.lang, f'custom_sort_{args.lang}_prompt.md')
    
    prompt_content = load_file(prompt_file_path)
    if prompt_content is None:
        print("**FATAL ERROR:** Prompt file not found or could not be read.\n")
        sys.exit(1)
    
    print(f"## Prompt File Used\n`{os.path.basename(prompt_file_path)}`\n\n")

    llm_response = query_ollama(prompt_content, args.model)
    if not llm_response:
        print("**Overall Result: FAILURE (Query failed)**\n")
        sys.exit(1)

    print(f"## Raw LLM Response\n```\n{llm_response}\n```\n\n")

    final_code = extract_python_code(llm_response)
    if not final_code:
        print("**Overall Result: FAILURE (Code extraction failed)**\n")
        sys.exit(1)

    try:
        with open(solution_path, 'w', encoding='utf-8') as f:
            f.write(final_code)
        print(f"Content for final `{os.path.basename(solution_path)}` saved.\n\n")
    except IOError as e:
        print(f"**Overall Result: FAILURE (Failed to write solution file: {e})**\n")
        sys.exit(1)

    passed, pytest_output = run_pytest(args.output_dir)
    print(f"## Pytest Validation Result\nPassed: {passed}\n```\n{pytest_output}\n```\n")
    
    if passed:
        print("**Overall Result: SUCCESS**\n")
        sys.exit(0)
    else:
        print("**Overall Result: FAILURE**\n")
        sys.exit(1)

def load_file(filepath: str) -> Optional[str]:
    """Loads content from a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"**ERROR:** File not found: {filepath}", file=sys.stderr)
        return None
    except IOError as e:
        print(f"**ERROR:** Could not read file {filepath}: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    main()
