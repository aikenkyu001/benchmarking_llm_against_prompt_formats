import os
import sys
import requests
import re
import subprocess
import argparse
from datetime import datetime
from typing import Optional, Tuple

# --- Configuration ---
OLLAMA_API_URL = None

def query_ollama(prompt: str, model_name: str) -> Optional[str]:
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
    print("### Parsing LLM Response for Python function")
    
    # Make 'python' optional in the markdown fence
    code_blocks = re.findall(r"```(?:python)?\s*(.*?)\s*```", llm_response, re.DOTALL)
    if code_blocks:
        return code_blocks[0].strip()
    
    # Fallback for responses without markdown fences
    match = re.search(r"def\s+\w+\s*\(.*\):.*?(?:(?=^[ \t]*def\s+\w+\s*\()|(?=\n\S)|\Z)", llm_response, re.MULTILINE | re.DOTALL)
    if match:
        return match.group(0).strip()
        
    print("**ERROR:** Could not find a Python function in the LLM response.")
    return None

def run_pytest(output_dir: str, task_name: str) -> Tuple[bool, str]:
    print(f"### Running Pytest Validation for {task_name}")
    
    static_test_path = os.path.join(os.path.dirname(__file__), '..', '06_TestDefinitions', f'test_{task_name}.py')
    if not os.path.exists(static_test_path):
        return False, f"Static test file not found: {static_test_path}"

    test_dest_path = os.path.join(output_dir, 'test_generated_code.py')
    try:
        with open(static_test_path, 'r', encoding='utf-8') as f_src, open(test_dest_path, 'w', encoding='utf-8') as f_dst:
            f_dst.write(f_src.read())
    except IOError as e:
        return False, f"Could not copy test definition file: {e}"

    env = os.environ.copy()
    pythonpath = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = f"{output_dir}{os.pathsep}{pythonpath}"

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", test_dest_path],
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
    parser = argparse.ArgumentParser(description="Run a simple code generation task.")
    parser.add_argument("--output-dir", required=True, help="Directory to save generated files.")
    parser.add_argument("--ollama-url", required=True, help="Ollama API URL.")
    parser.add_argument("-m", "--model", required=True, help="The name of the Ollama model to test.")
    parser.add_argument("--lang", required=True, help="Language of the prompt.")
    parser.add_argument("--style", required=True, help="Style of the prompt (imperative or conversational).")
    args = parser.parse_args()

    global OLLAMA_API_URL
    OLLAMA_API_URL = args.ollama_url

    script_name = os.path.basename(sys.argv[0])
    task_name = script_name.replace('run_', '').replace('_test.py', '')

    print(f"# Simple Task Log for {args.model}\n\n**Task:** {task_name}\n**Date:** {datetime.now().isoformat()}\n**Lang:** {args.lang}\n**Style:** {args.style}\n")

    os.makedirs(args.output_dir, exist_ok=True)
    solution_path = os.path.join(args.output_dir, 'generated_code.py')
    
    prompt_file_path = os.path.join(os.path.dirname(__file__), '..', '04_Prompts', args.lang, f'{task_name}_{args.lang}_{args.style}.md')

    try:
        with open(prompt_file_path, 'r', encoding='utf-8') as f:
            prompt_content = f.read()
    except FileNotFoundError:
        print(f"**FATAL ERROR:** Prompt file not found: {prompt_file_path}")
        sys.exit(1)

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
        sys.exit(f"**Overall Result: ❌ FAILURE (Failed to write solution file: {e})")

    passed, pytest_output = run_pytest(args.output_dir, task_name)
    
    if passed:
        print(f"**Overall Result for `{args.model}` on task `{task_name}`: 🎉 SUCCESS**")
        sys.exit(0)
    else:
        print(f"**Overall Result for `{args.model}` on task `{task_name}`: ❌ FAILURE**")
        sys.exit(1)

if __name__ == "__main__":
    main()
