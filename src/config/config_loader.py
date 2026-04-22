import yaml
from pathlib import Path

from models.config_models import ModelConfig 

ROOT = Path(__file__).resolve().parent.parent

def load_config(path= ROOT / "config/config.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    return ModelConfig(
        models = config["models"],
        judgeModel = config["model"]["judge"],
        max_tokens = config["llm"].get("max_tokens", 150),
        temperature = config["llm"].get("temperature", 0.2)
    )