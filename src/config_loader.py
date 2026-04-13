import yaml
from pathlib import Path 

ROOT = Path(__file__).resolve().parent.parent

def load_config(path= ROOT / "config.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)