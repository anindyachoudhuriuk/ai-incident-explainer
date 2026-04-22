from config.config_loader import load_config
from llms.llm_client import call_llm
from llms.prompt_loader import load_judge_prompt
from models.response_models import JudgeSchema
import json
    
def build_prompt(judge_prompt, evaluated_output):
    
    data = {
    "incident": f"{evaluated_output['id']}: summary: {evaluated_output['summary']}",
    "response": f"{evaluated_output['what_happened']} Root cause: {evaluated_output['root_cause']}"
    }

    judge_prompt = json.dumps(data, indent=2)
    return judge_prompt

def judge_response(response)-> int:
 
    config = load_config()
    judge_prompt = load_judge_prompt()
    prompt = build_prompt(judge_prompt, response)
           
    response = call_llm(config.judgeModel, prompt, JudgeSchema)
    json_data = json.loads(response.json())
        
    return {
        "relevance" : json_data.get("relevance"),
        "details" : (json_data.get("completeness") + json_data.get("clarity"))/2
        }

    