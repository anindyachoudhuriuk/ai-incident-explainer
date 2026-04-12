import requests
import time

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1"

def call_llm(prompt: str) -> str:
    print("\n📤 Sending request to Ollama...")
    print(f"Prompt preview:\n{prompt[:200]}...\n")

    start = time.time()

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        raise Exception(f"LLM error: {response.text}")
    end = time.time()
    print(f"Response time: {end - start:.2f} seconds")
    return response.json()["response"]