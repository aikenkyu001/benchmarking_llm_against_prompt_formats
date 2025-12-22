import os
import sys
import requests
import json
import re
import subprocess
import time
import argparse
from datetime import datetime
from typing import Optional, Tuple, Dict, Any

# --- Configuration ---
OLLAMA_API_URL = None
MAX_RETRIES = 3

# --- File Paths ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AGI_DISTANT_BEYOND_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, '..'))
PROMPT_FILE = os.path.join(AGI_DISTANT_BEYOND_DIR, '04_Prompts', 'prompt_final_symbolic_sexpr.md')

# --- Helper Functions ---

def query_ollama(prompt: str, model_name: str) -> Optional[str]:
    """Sends a prompt to the Ollama API and returns the response."""
    print(f"### Querying Model: `{model_name}`")
    try:
        response = requests.post(
            OLLAMA_API_URL,
            json={'model': model_name, 'prompt': prompt, 'stream': False, 'options': {'temperature': 0.0}},
            timeout=60
        )
        response.raise_for_status()
        llm_response = response.json().get('response', '').strip()
        print(f"#### Raw LLM Response:\n```\n{llm_response}\n```")
        return llm_response
    except requests.exceptions.RequestException as e:
        print(f"**ERROR:** API request failed: {e}")
        return None

def clean_and_split_code(llm_response: str, main_path: str, test_path: str) -> bool:
    """Parses the LLM response to extract and write main and test code files."""
    print("### Parsing LLM Response")
    
    main_marker = "# main.py"
    test_marker = "# test_main.py"

    main_pos = llm_response.find(main_marker)
    test_pos = llm_response.find(test_marker)

    if main_pos == -1 or test_pos == -1:
        print(f"**ERROR:** Could not find both '{main_marker}' and '{test_marker}' in the response.")
        return False

    # Assume main.py comes before test_main.py
    if main_pos < test_pos:
        main_code_raw = llm_response[main_pos + len(main_marker) : test_pos]
        test_code_raw = llm_response[test_pos + len(test_marker) :]
    else: # Should not happen based on prompt, but handle it
        test_code_raw = llm_response[test_pos + len(test_marker) : main_pos]
        main_code_raw = llm_response[main_pos + len(main_marker) :]

    # Clean up potential markdown fences from the snippets
    main_code = re.sub(r"```python\s*|\s*```", "", main_code_raw).strip()
    test_code = re.sub(r"```python\s*|\s*```", "", test_code_raw).strip()

    if not main_code or not test_code:
        print("**ERROR:** Extracted code for main.py or test_main.py is empty.")
        return False

    try:
        with open(main_path, 'w', encoding='utf-8') as f: f.write(main_code)
        print(f"Content for `{os.path.basename(main_path)}` saved.")
        with open(test_path, 'w', encoding='utf-8') as f: f.write(test_code)
        print(f"Content for `{os.path.basename(test_path)}` saved.")
        return True
    except IOError as e:
        print(f"**ERROR:** Failed to write split files: {e}")
        return False

def run_pytest(test_path: str) -> Tuple[bool, str]:
    """Runs pytest and returns success status and output."""
    print("### Running Pytest Validation")
    test_dir = os.path.dirname(test_path)
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", os.path.basename(test_path)],
            capture_output=True, text=True, cwd=test_dir, timeout=60
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

def execute_test_run(model: str, prompt: str, main_path: str, test_path: str) -> bool:
    """Executes a single, self-correcting test run."""
    current_prompt = prompt
    for attempt in range(MAX_RETRIES):
        print(f"--- \n### ATTEMPT {attempt + 1}/{MAX_RETRIES}")
        llm_response = query_ollama(current_prompt, model)
        if not llm_response:
            print("**Query failed. Retrying...**")
            continue
        
        if not clean_and_split_code(llm_response, main_path, test_path):
            print("**Attempting to fix formatting error: LLM did not follow output rules.**")
            current_prompt = f"The previous response did not follow the CRITICAL OUTPUT RULES, specifically for '# main.py' and '# test_main.py' code blocks.\nOriginal prompt:\n---\n{prompt}\n---\nPrevious invalid response:\n---\n{llm_response}\n---\n**Please regenerate the response strictly adhering to the CRITICAL OUTPUT RULES for code blocks." 
            continue

        passed, pytest_output = run_pytest(test_path)
        if passed:
            return True

        if attempt < MAX_RETRIES - 1:
            print("**Attempting to fix pytest error...**")
            try:
                main_code = open(main_path, 'r', encoding='utf-8').read()
                test_code = open(test_path, 'r', encoding='utf-8').read()
            except IOError as e:
                print(f"Could not read generated files for self-correction: {e}")
                main_code, test_code = "", ""
                
            current_prompt = f"The code you generated failed pytest validation.\nOriginal prompt:\n---\n{prompt}\n---\nYour code:\n---\n# main.py\n{main_code}\n\n# test_main.py\n{test_code}\n---\nThe error:\n---\n{pytest_output}\n---\n**Please analyze the error and regenerate the Python code to fix it, strictly adhering to the CRITICAL OUTPUT RULES for output format."
    return False

def main():
    """Orchestrates the final symbolic benchmark."""
    parser = argparse.ArgumentParser(description="Run the final symbolic S-expression benchmark for a given model.")
    parser.add_argument("--output-dir", required=True, help="Directory to save generated files.")
    parser.add_argument("--ollama-url", default=os.getenv('OLLAMA_API_URL'), help="Ollama API URL.")
    parser.add_argument("-m", "--model", default='gemma:2b', help="The name of the Ollama model to test.")
    args = parser.parse_args()
    
    global OLLAMA_API_URL
    OLLAMA_API_URL = args.ollama_url
    if OLLAMA_API_URL and not OLLAMA_API_URL.endswith(('/api/generate', '/api/chat')):
        OLLAMA_API_URL = OLLAMA_API_URL.rstrip('/') + '/api/generate'

    if OLLAMA_API_URL is None:
        sys.exit("Error: Ollama API URL must be provided via --ollama-url or OLLAMA_API_URL environment variable.")

    model = args.model
    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    main_path = os.path.join(output_dir, 'main.py')
    test_path = os.path.join(output_dir, 'test_main.py')

    print(f"# Final Symbolic S-expression Benchmark Log for {model}\n\n**Date:** {datetime.now().isoformat()}\n")

    try:
        with open(PROMPT_FILE, 'r', encoding='utf-8') as f:
            prompt_content = f.read()
    except FileNotFoundError:
        print(f"**FATAL ERROR:** Main prompt file not found: {PROMPT_FILE}")
        sys.exit(1)

    final_result = execute_test_run(model, prompt_content, main_path, test_path)
    
    if final_result:
        print(f"**Overall Result for `{model}`: 🎉 SUCCESS**")
        print(f"\nTest for {model} finished successfully.")
        sys.exit(0)
    else:
        print(f"**Overall Result for `{model}`: ❌ FAILURE**")
        print(f"\nTest for {model} finished with failures.")
        sys.exit(1)

if __name__ == "__main__":
    main()
