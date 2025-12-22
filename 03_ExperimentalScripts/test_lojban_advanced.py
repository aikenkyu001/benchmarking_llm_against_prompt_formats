
import requests
import json
import re
import io
import contextlib
import argparse

# --- Sentence Definitions ---
LOJBAN_SENTENCE = "lo gerku cu sutra" # The dog is fast
ENGLISH_SENTENCE = "The dog is fast"
JAPANESE_SENTENCE = "犬は速い"
ESPERANTO_SENTENCE = "La hundo estas rapida"

# --- Lojban Code Generation Prompt ---
# From /home/miyata/project/sigmasensejp/tools/llm_reliability_tester/slm_armor/benchmarking_llm_against_prompt_formats/04_Prompts/jbo/return_one_jbo_imperative.md
LOJBAN_CODE_PROMPT = """GUNMA: .i ko zbasu lo python funkci'o

- FUNKCI'O CMENE: `execute`
- FUNCI'O PAMOI: (nodau)
- JONAI: .i ko velsi'a lo namcu po'u li 1
"""
# Note: Changed 'return_one' to 'execute' in LOJBAN_CODE_PROMPT for consistency
# with the paper's execute function definition.

# --- Test Cases ---
TEST_CASES = [
    {
        "id": "jbo_to_en_translation",
        "prompt": f"Translate the Lojban sentence \"{LOJBAN_SENTENCE}\" into English. Return only the translation.",
        "expected_keywords": ["dog", "fast"],
        "validation_type": "keywords"
    },
    {
        "id": "jbo_to_ja_translation",
        "prompt": f"\"{LOJBAN_SENTENCE}\"というロジバン文を日本語に翻訳してください。翻訳結果のみを返してください。",
        "expected_keywords": ["犬", "速い"],
        "validation_type": "keywords"
    },
    {
        "id": "jbo_to_eo_translation",
        "prompt": f"Traduku la lojbanan frazon \"{LOJBAN_SENTENCE}\" al Esperanto. Redonu nur la tradukon.",
        "expected_keywords": ["hundo", "rapida"],
        "validation_type": "keywords"
    },
    {
        "id": "en_to_jbo_translation",
        "prompt": f"Translate the English sentence \"{ENGLISH_SENTENCE}\" into Lojban. Return only the Lojban translation.",
        "expected_keywords": ["gerku", "sutra"],
        "validation_type": "keywords"
    },
    {
        "id": "ja_to_jbo_translation",
        "prompt": f"\"{JAPANESE_SENTENCE}\"という日本語の文をロジバンに翻訳してください。ロジバン訳のみを返してください。",
        "expected_keywords": ["gerku", "sutra"],
        "validation_type": "keywords"
    },
    {
        "id": "eo_to_jbo_translation",
        "prompt": f"Traduku la Esperantan frazon \"{ESPERANTO_SENTENCE}\" al Lojban. Redonu nur la lojbanan tradukon.",
        "expected_keywords": ["gerku", "sutra"],
        "validation_type": "keywords"
    },
    {
        "id": "jbo_to_code_return_one",
        "prompt": LOJBAN_CODE_PROMPT,
        "expected_return_value": 1,
        "validation_type": "python_execution"
    }
]

# --- Helper function for Python code execution ---
@contextlib.contextmanager
def nostdout():
    save_stdout = io.StringIO()
    with contextlib.redirect_stdout(save_stdout):
        yield

def execute_python_code(code_string):
    """
    Extracts and executes Python code from a string, expecting an 'execute' function
    that takes no arguments and returns a value.
    Returns the value of execute() or an exception.
    """
    # Use regex to find python code blocks
    python_code_blocks = re.findall(r"```python\n(.*?)\n```", code_string, re.DOTALL)
    if not python_code_blocks:
        # If no markdown block, assume the entire response is code
        python_code = code_string
    else:
        # If multiple, use the first one. If a model generates text before the code block, this handles it.
        python_code = python_code_blocks[0]

    if "def execute():" not in python_code:
        return ValueError("No 'def execute():' function found in the generated code.")

    # Prepare a safe execution environment
    exec_globals = {}
    exec_locals = {}
    
    # Capture stdout during execution
    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        try:
            # Execute the code
            exec(python_code, exec_globals, exec_locals)
            
            # Call the 'execute' function
            if 'execute' in exec_locals:
                result = exec_locals['execute']()
                return result
            else:
                return ValueError("The 'execute' function was not defined or accessible.")
        except Exception as e:
            return e # Return the exception for analysis

def call_ollama_api(url, model, prompt_content, temperature=0.0):
    """
    Calls the Ollama chat API using the requests library.
    """
    api_endpoint = f"{url.rstrip('/')}/api/chat"
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt_content
            }
        ],
        "stream": False,
        "options": {
            "temperature": temperature
        }
    }
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(api_endpoint, json=payload, headers=headers, timeout=60)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}

def run_advanced_test(ollama_url, model):
    """
    Runs the advanced Lojban understanding and code generation tests for a single model.
    """
    model_results = {}
    print(f"--- Starting Advanced Lojban Tests for Model: {model} ---")
    
    for test_case in TEST_CASES:
        print(f"  Running test: {test_case['id']}...")
        try:
            response_data = call_ollama_api(ollama_url, model, test_case['prompt'])
            
            success = False
            detail = ""

            if "error" in response_data:
                success = False
                content = response_data["error"]
                detail = f"API call failed: {content}"
            else:
                content = response_data.get('message', {}).get('content', '')
                if test_case["validation_type"] == "keywords":
                    # For translation tasks, check for expected keywords
                    success = all(kw.lower() in content.lower() for kw in test_case['expected_keywords'])
                    detail = f"Expected: {test_case['expected_keywords']}, Received: {content.strip()}"
                elif test_case["validation_type"] == "python_execution":
                    # For code generation tasks, execute and check return value
                    execution_result = execute_python_code(content)
                    if isinstance(execution_result, Exception):
                        success = False
                        detail = f"Execution failed with error: {execution_result}. Generated code: {content.strip()}"
                    else:
                        success = (execution_result == test_case['expected_return_value'])
                        detail = f"Expected return: {test_case['expected_return_value']}, Actual return: {execution_result}. Generated code: {content.strip()}"
            
            print(f"    Success: {success}")
            model_results[test_case['id']] = {
                "success": success,
                "response": content,
                "detail": detail
            }

        except Exception as e:
            print(f"    Error during test {test_case['id']}: {e}")
            model_results[test_case['id']] = {
                "success": False,
                "response": str(e),
                "detail": f"An unexpected error occurred: {e}"
            }
    
    # Print final JSON result for this model to stdout
    print(json.dumps(model_results, ensure_ascii=False))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run advanced Lojban understanding and code generation tests against an Ollama model.")
    parser.add_argument("--ollama-url", default="http://10.5.42.169:11434", help="URL of the Ollama API server.")
    parser.add_argument("--model", required=True, help="Name of the model to test (e.g., 'llama3:8b').")
    
    args = parser.parse_args()
    
    run_advanced_test(args.ollama_url, args.model)
