
from pydantic import BaseModel
import requests
import time

from torch import Type
from config.config_loader import load_config

config = load_config()
OLLAMA_URL = "http://localhost:11434/api/generate"

def call_llm(model: str, prompt: str, schema : Type[BaseModel]) -> str:
    print("\n📤 Sending request to Ollama with model: " + model + " , response schema: " + schema.__name__)
    
    start = time.time()
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "format": schema.model_json_schema(),
         "options": {
            "num_predict": config.max_tokens,
            "temperature": config.temperature
        }
    }

    response = requests.post(OLLAMA_URL, json=payload)
    if response.status_code != 200:
        raise Exception(f"LLM error: {response.text}")
    response = schema.model_validate_json(response.json()["response"])
    
    end = time.time()
    print(f"Response time: {end - start:.2f} seconds")
    response.__setattr__("model", model)
    response.__setattr__("latency_ms", (end - start) * 1000)  # add latency in ms for evaluation
    return response