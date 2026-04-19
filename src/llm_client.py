
import requests
import time

from config_loader import load_config
from models.config_models import ModelConfig
from models.response_models import ResponseSchema

OLLAMA_URL = "http://localhost:11434/api/generate"

def call_llm(config: ModelConfig, prompt: str) -> str:
    print("\n📤 Sending request to Ollama...")

    start = time.time()
    
    payload = {
        "model": config.model,
        "prompt": prompt,
        "stream": False,
        "format": ResponseSchema.model_json_schema(),
         "options": {
            "num_predict": config.max_tokens,
            "temperature": config.temperature
        }
    }

    response = requests.post(OLLAMA_URL, json=payload)
    if response.status_code != 200:
        raise Exception(f"LLM error: {response.text}")
    
    response = ResponseSchema.model_validate_json(response.json()["response"])
    
    end = time.time()
    print(f"Response time: {end - start:.2f} seconds")
    response.__setattr__("latency_ms", (end - start) * 1000)  # add latency in ms for evaluation
    return response