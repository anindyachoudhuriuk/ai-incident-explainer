
from pathlib import Path 
ROOT = Path(__file__).resolve().parent.parent
    
def load_incident_prompt():
    with open(ROOT / "prompts" / "incident_prompt_template.txt", "r") as f:
        return f.read()
    
def load_judge_prompt():
    with open(ROOT / "prompts" / "judge_prompt_template.txt", "r") as f:
        return f.read()