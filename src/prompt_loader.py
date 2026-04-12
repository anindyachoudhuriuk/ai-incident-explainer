
def load_system_prompt():
    with open('prompts/system_prompt.txt', 'r') as f:
        return f.read()
    
def load_template():
    with open('prompts/incident_prompt_template.txt', 'r') as f:
        return f.read()