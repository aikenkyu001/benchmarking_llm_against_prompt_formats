import argparse
import os
import sys
import requests
import json
import re
from datetime import datetime
from typing import Optional, List

# --- Configuration ---
OLLAMA_API_URL = None
DEFAULT_MODEL_NAME = 'tinydolphin:latest'
TIMEOUT = 60 # seconds

def load_file(filepath: str) -> Optional[str]:
    """Loads a file and returns its content."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error loading file {filepath}: {e}", file=sys.stderr)
        return None

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
        print(f"#### Raw LLM Response (first 500 chars):\n```\n{llm_response[:500]}...\n```")
        return llm_response
    except requests.exceptions.RequestException as e:
        print(f"**ERROR:** API request failed: {e}", file=sys.stderr)
        return None
    except json.JSONDecodeError:
        print(f"**ERROR:** Failed to decode JSON from response: {response.text}", file=sys.stderr)
        return None

def extract_list_from_raw_response(llm_response: str) -> Optional[List[int]]:
    """
    Attempts to extract a Python list from the raw LLM response.
    Returns None if the response contains other text/code or if parsing fails.
    This function is strict: the response must ONLY be a list.
    """
    print(f"### Attempting to extract list directly from raw response (strictly): '{llm_response[:100]}...'")

    # Check for presence of code blocks, function definitions, or print statements
    # and any other non-whitespace, non-list characters outside the list pattern
    if re.search(r"```(?:python)?\s*", llm_response, re.DOTALL) or \
       re.search(r"def\s+\w+\s*\(.*\)", llm_response) or \
       re.search(r"print\s*\(.*\)", llm_response):
        print("**INFO:** Raw response contains code-like patterns. Treating as instruction violation.")
        return None
    
    # Strictly match the entire response as a list pattern, allowing for leading/trailing whitespace
    match = re.fullmatch(r'\s*(\[\s*(?:\-?\d+\s*,\s*)*\-?\d*\s*\])\s*', llm_response, re.DOTALL)
    if not match:
        print("**INFO:** Raw response does not match expected strict list format or contains extraneous text.")
        return None
    
    list_str = match.group(1) # Extract just the list part
    try:
        extracted_list = json.loads(list_str)
        if not isinstance(extracted_list, list):
             print(f"**INFO:** Extracted object is not a list: {extracted_list}")
             return None
        print(f"**INFO:** Successfully extracted strict list: {extracted_list}")
        return extracted_list
    except (json.JSONDecodeError, ValueError) as e:
        print(f"**ERROR:** Failed to parse extracted list from response '{list_str}': {e}", file=sys.stderr)
        return None

def main():
    parser = argparse.ArgumentParser(description="Run a filtered list test with strict direct list evaluation.")
    parser.add_argument("--output-dir", required=True, help="Directory to save logs and results.")
    parser.add_argument("--ollama-url", default=os.getenv('OLLAMA_API_URL'), help="Ollama API URL.")
    parser.add_argument("-m", "--model", default=DEFAULT_MODEL_NAME, help=f"The LLM model to use (default: {DEFAULT_MODEL_NAME})")
    parser.add_argument("--prompt-file", required=True, help="Path to the prompt file for the filtered list task.")
    
    args = parser.parse_args()

    global OLLAMA_API_URL
    OLLAMA_API_URL = args.ollama_url
    if OLLAMA_API_URL and not OLLAMA_API_URL.endswith(('/api/generate', '/api/chat')):
        OLLAMA_API_URL = OLLAMA_API_URL.rstrip('/') + '/api/generate'

    if OLLAMA_API_URL is None:
        sys.exit("Error: Ollama API URL must be provided via --ollama-url or OLLAMA_API_URL environment variable.")

    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)
    
    log_filepath = os.path.join(output_dir, f"filtered_list_log_{args.model.replace(':', '_')}.md")
    results_filepath = os.path.join(output_dir, f"filtered_list_results_{args.model.replace(':', '_')}.json")

    prompt_content = load_file(args.prompt_file)
    if prompt_content is None:
        sys.exit(1)

    with open(log_filepath, 'w', encoding='utf-8') as log_file:
        log_file.write(f"# Filtered List Test Log for {args.model}\n\n**Date:** {datetime.now().isoformat()}\n\n")
        log_file.write("## Prompt Used\n```\n")
        log_file.write(prompt_content)
        log_file.write("\n```\n\n")

        llm_response = query_ollama(prompt_content, args.model)
        if llm_response is None:
            log_file.write("**Result: ❌ FAILURE (API Query Error)**\n")
            sys.exit(1)

        log_file.write(f"## Raw LLM Response\n```\n{llm_response}\n```\n\n")

        # --- Strict Direct List Evaluation Logic ---
        is_correct = False
        extracted_list = None
        expected_list = [2, 4, 6, 10]
        
        extracted_list = extract_list_from_raw_response(llm_response)

        # Final check
        if extracted_list is not None:
            is_correct = sorted(extracted_list) == sorted(expected_list)

        log_file.write(f"## Evaluation\n- **Extracted List:** `{extracted_list}`\n- **Expected List:** `{expected_list}`\n- **Correct:** {is_correct}\n\n")

        # --- Final Result ---
        final_result_data = {
            "model": args.model,
            "prompt_file": os.path.basename(args.prompt_file),
            "timestamp": datetime.now().isoformat(),
            "llm_response_full": llm_response,
            # Removed code execution related data as it's no longer relevant
            "extracted_code": None,
            "execution_stdout": None,
            "execution_stderr": None,
            "extracted_list": extracted_list,
            "expected_list": expected_list,
            "is_correct": is_correct
        }
        
        with open(results_filepath, 'w', encoding='utf-8') as res_file:
            json.dump(final_result_data, res_file, ensure_ascii=False, indent=2)

        if is_correct:
            log_file.write(f"**Overall Result: ✅ SUCCESS**\n")
            print("Overall Result: SUCCESS")
            sys.exit(0)
        else:
            log_file.write(f"**Overall Result: ❌ FAILURE**\n")
            print("Overall Result: FAILURE")
            sys.exit(1)

if __name__ == "__main__":
    main()
