import requests
import time

from config_loader import load_config
OLLAMA_URL = "http://localhost:11434/api/generate"

config = load_config()
MODEL = config["model"]["name"]
TEMPERATURE = config["llm"].get("temperature", 0.2)
MAX_TOKENS = config["llm"].get("max_tokens", 150)  # default fallback

def call_llm(prompt: str) -> str:
    print("\n📤 Sending request to Ollama...")

    start = time.time()

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
         "options": {
            "num_predict": MAX_TOKENS,
            "temperature": TEMPERATURE
        }
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code != 200:
        raise Exception(f"LLM error: {response.text}")
    end = time.time()
    print(f"Response time: {end - start:.2f} seconds")
    return response.json()["response"]