from pathlib import Path
import time
from utils import save_json
from utils import load_json
from processor import process_incident 
from evaluation.evaluator import evaluate_output
from evaluation.scorer import compute_final_score
from config_loader import load_config

def main():
    print("🚀 AI Incident Explainer starting...")
    start = time.time()
    ROOT = Path(__file__).resolve().parent.parent
    incidents = load_json(ROOT / "data" / "incident_logs.json")
    print(f"Loaded {len(incidents)} incidents.")
    config = load_config()
    results = [] 
    MODEL = config["model"]["name"]
    for i in incidents:
        print(f"Processing incident: {i['id']}")
         # Step 1: LLM processing
        result = process_incident(i, MODEL)

        # Step 3: Evaluate
        metrics = evaluate_output(result)

        # Step 4: Score
        final_score = compute_final_score(metrics)

        # Step 5: Attach evaluation to result
        result["evaluation"] = {
            "model": MODEL,
            "metrics": metrics.model_dump(),
            "final_score": final_score
        }

        results.append(result)

    save_json(results, ROOT / "outputs" / "sample_run.json")
    end = time.time()
    print(f"Total time: {end - start:.2f} seconds")
    print("✅ Done. Results saved in outputs/sample_run.json")

if __name__ == "__main__":
    main()
    