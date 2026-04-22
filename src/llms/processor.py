import json

from llms.prompt_loader import load_incident_prompt
from models.response_models import ResponseSchema
from llms.llm_client import call_llm

def build_prompt(incident_prompt, incident):
    
    data = {
    "system": f"{incident['system']}",
    "error": f"{incident['error']}",
    "context": f"{incident['context']}"
    }

    incident_prompt = json.dumps(data, indent=2)
    return incident_prompt

def process_incident(incident, model):
    # Placeholder for actual processing logic
    # For now, just return a dummy result
    
    incident_prompt = load_incident_prompt()
    prompt = build_prompt(incident_prompt, incident)
           
    response = call_llm(model, prompt, ResponseSchema)
    json_data = json.loads(response.json())
        
    return {
    "id": incident.get("id"),
    "summary": f"Summary of incident {incident.get('id')}",
    "what_happened": json_data.get("analysis", {}).get("what_happened"),
    "root_cause": get_first_root_cause(json_data),
    "model": json_data.get("model"),
    "latency_ms": json_data.get("latency_ms")
}
    
def get_first_root_cause(json_data):
    try:
        return json_data["analysis"]["root_causes"][0]["cause"]
    except (KeyError, IndexError, TypeError):
        return None