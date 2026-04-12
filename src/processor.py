


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
    
    system_prompt = load_system_prompt()
    template = load_template()
    prompt = build_prompt(system_prompt, template, incident)
           
    response = call_llm(prompt)

    return {
        "id": incident['id'],
        "summary": f"Summary of incident {incident['id']}",
        "root_cause": "Root cause analysis goes here.",
        "recommendations": response
    }