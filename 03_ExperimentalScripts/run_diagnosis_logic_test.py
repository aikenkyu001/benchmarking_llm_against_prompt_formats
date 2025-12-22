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
MAX_RETRIES = 1

# --- File Paths ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AGI_DISTANT_BEYOND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))
TEST_DEFINITION_FILE = os.path.join(AGI_DISTANT_BEYOND_DIR, '06_TestDefinitions', 'test_diagnosis_logic.py')

def query_ollama(prompt: str, model_name: str) -> Optional[str]:
    """Sends a prompt to the Ollama API and returns the response."""
    print(f"### Querying Model: `{model_name}`")
    try:
        response = requests.post(
            OLLAMA_API_URL,
            json={'model': model_name, 'prompt': prompt, 'stream': False, 'options': {'temperature': 0.0}},
            timeout=120
        )
        response.raise_for_status()
        llm_response = response.json().get('response', '').strip()
        print(f"#### Raw LLM Response (first 100 chars):\n```\n{llm_response[:100]}...\n```")
        return llm_response
    except requests.exceptions.RequestException as e:
        print(f"**ERROR:** API request failed: {e}")
        return None

def extract_python_code(llm_response: str) -> Optional[str]:
    """Parses the LLM response to extract the Python code for the diagnose function."""
    print("### Parsing LLM Response for diagnose() function")
    
    code_blocks = re.findall(r"```python\s*(.*?)\s*```", llm_response, re.DOTALL)
    if code_blocks:
        code_to_parse = code_blocks[0].strip()
    else:
        code_to_parse = llm_response

    match = re.search(r"def diagnose\s*\(\s*symptoms\s*:\s*list\s*\)\s*->\s*str\s*:.*?(?:(?=^[ \t]*def\s+\w+\s*\()|(?=\n\S)|\Z)", code_to_parse, re.MULTILINE | re.DOTALL)
    if match:
        print("**INFO:** Successfully extracted 'diagnose()' function.")
        return match.group(0).strip()
    
    print("**ERROR:** Could not find a complete 'def diagnose(...):' function in the LLM response.")
    return None

def run_pytest(output_dir: str) -> Tuple[bool, str]:
    """Runs pytest on the generated code and the static test definition."""
    print("### Running Pytest Validation")
    try:
        static_test_content = open(TEST_DEFINITION_FILE, 'r', encoding='utf-8').read()
        with open(os.path.join(output_dir, 'test_diagnosis_logic.py'), 'w', encoding='utf-8') as f:
            f.write(static_test_content)
    except IOError as e:
        print(f"**ERROR:** Could not copy test definition file: {e}")
        return False, str(e)

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
    """Orchestrates the Diagnosis Logic benchmark."""
    parser = argparse.ArgumentParser(description="Run a diagnosis logic benchmark for a given model.")
    parser.add_argument("--output-dir", required=True, help="Directory to save logs and generated files.")
    parser.add_argument("--ollama-url", default=os.getenv('OLLAMA_API_URL'), help="Ollama API URL.")
    parser.add_argument("-m", "--model", default='gemma:2b', help="The name of the Ollama model to test.")
    parser.add_argument("--test-type", choices=['s_expr', 'json', 'tsv', 'token_test'], default='s_expr', help="The type of prompt format to use.")
    
    args = parser.parse_args()
    
    global OLLAMA_API_URL
    OLLAMA_API_URL = args.ollama_url
    if OLLAMA_API_URL and not OLLAMA_API_URL.endswith(('/api/generate', '/api/chat')):
        OLLAMA_API_URL = OLLAMA_API_URL.rstrip('/') + '/api/generate'

    if OLLAMA_API_URL is None:
        sys.exit("Error: Ollama API URL must be provided via --ollama-url or OLLAMA_API_URL environment variable.")

    os.makedirs(args.output_dir, exist_ok=True)
    solution_path = os.path.join(args.output_dir, 'diagnosis_logic.py')

    print(f"# Diagnosis Logic Test Log for {args.model}\n\n**Date:** {datetime.now().isoformat()}\n**Test Type:** {args.test_type}\n")

    # --- Determine Prompt File ---
    prompt_file_path = os.path.join(AGI_DISTANT_BEYOND_DIR, '04_Prompts', f'prompt_diagnosis_logic_{args.test_type}.md')
    
    try:
        with open(prompt_file_path, 'r', encoding='utf-8') as f:
            prompt_content = f.read()
    except FileNotFoundError:
        print(f"**FATAL ERROR:** Prompt file not found: {prompt_file_path}")
        sys.exit(1)

    # --- Execute Test ---
    llm_response = query_ollama(prompt_content, args.model)
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
        sys.exit(f"**Overall Result: ❌ FAILURE (Failed to write solution file: {e})**")

    passed, pytest_output = run_pytest(args.output_dir)
    
    if passed:
        print(f"**Overall Result for `{args.model}`: 🎉 SUCCESS**")
        sys.exit(0)
    else:
        print(f"**Overall Result for `{args.model}`: ❌ FAILURE**")
        sys.exit(1)

if __name__ == "__main__":
    main()