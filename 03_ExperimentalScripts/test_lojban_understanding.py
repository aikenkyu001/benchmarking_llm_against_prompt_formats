
import requests
import json
import argparse

# Define the prompt and expected keywords at a global level
PROMPT = "Translate the Lojban sentence \"lo gerku cu sutra\" into English. Return only the translation."
EXPECTED_KEYWORDS = ["dog", "fast"]

def call_ollama_api(url, model, prompt, temperature=0.0):
    """
    Calls the Ollama chat API using the requests library.
    """
    # Ensure the URL doesn't have a trailing slash before appending the path
    api_endpoint = f"{url.rstrip('/')}/api/chat"
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
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
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}

def run_test(ollama_url, model):
    """
    Runs the Lojban understanding test on a single specified model
    and prints the result as a JSON object to stdout.
    """
    print(f"--- Starting Lojban Understanding Test on {model} ---")
    
    response_data = call_ollama_api(ollama_url, model, PROMPT)
    
    if "error" in response_data:
        success = False
        content = response_data["error"]
        print(f"  Error: {content}")
    else:
        content = response_data.get('message', {}).get('content', '')
        success = all(keyword.lower() in content.lower() for keyword in EXPECTED_KEYWORDS)
        print(f"  Response: {content.strip()}")

    print(f"  Success: {success}")
    
    # Prepare the final result dictionary
    result = {"model": model, "success": success, "response": content}
    
    # Print final JSON result to stdout
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a Lojban understanding test against an Ollama model.")
    parser.add_argument("--ollama-url", default="http://10.5.42.169:11434", help="URL of the Ollama API server.")
    parser.add_argument("--model", required=True, help="Name of the model to test (e.g., 'llama3:8b').")
    
    args = parser.parse_args()
    
    run_test(args.ollama_url, args.model)
