
from pathlib import Path 
ROOT = Path(__file__).resolve().parent.parent

def load_system_prompt():
    with open(ROOT / "prompts" / "system_prompt.txt", "r") as f:
        return f.read()
    
def load_template():
    with open(ROOT / "prompts" / "incident_prompt_template.txt", "r") as f:
        return f.read()