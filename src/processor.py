


import json

from soupsieve import match


def build_prompt(system_prompt, template, incident):
    
    return f"""
{system_prompt}

{template.format(
    system=incident["system"],
    error=incident["error"],
    context=incident["context"]
)}
"""

def process_incident(incident):
    # Placeholder for actual processing logic
    # For now, just return a dummy result
    from llm_client import call_llm
    from prompt_loader import load_system_prompt, load_template
    import re, json
    
    system_prompt = load_system_prompt()
    template = load_template()
    prompt = build_prompt(system_prompt, template, incident)
           
    response = call_llm(prompt)
    print(f"LLM response: {response}")

    json_data = parse_llm_response(response)
    
    return {
    "id": incident.get("id"),
    "summary": f"Summary of incident {incident.get('id')}",
    "what_happened": json_data.get("analysis", {}).get("what_happened"),
    "root_cause": get_first_root_cause(json_data)
}
    
def get_first_root_cause(json_data):
    try:
        return json_data["analysis"]["root_causes"][0]["cause"]
    except (KeyError, IndexError, TypeError):
        return None
    
import re
import json

def parse_llm_response(response: str):
    match = re.search(r"```json\s*(\{.*?\})\s*```", response, re.DOTALL)
    if not match:
        return json.loads(response)
    
    json_str = match.group(1)
    return json.loads(json_str)