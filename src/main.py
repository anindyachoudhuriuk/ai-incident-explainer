from pathlib import Path
import time
from utils.utils import save_json, load_json, load_latest_leaderboard
from llms.processor import process_incident 
from evaluation.evaluator import evaluate_output
from evaluation.scorer import compute_final_score


def analyze_incidents():
    print("🚀 AI Incident Explainer starting...")
    start = time.time()
    ROOT = Path(__file__).resolve().parent.parent
    incidents = load_json(ROOT / "data" / "incident_logs.json")
    print(f"Loaded {len(incidents)} incidents.")
    results = [] 
    model = load_latest_leaderboard(ROOT)
    
    for i in incidents:
        print(f"Processing incident: {i['id']} with model: {model['best_model']}")
         # Step 1: LLM processing
        result = process_incident(i, model["best_model"])
        results.append(result)

    save_json(results, ROOT / "outputs" / "sample_run.json")
    end = time.time()
    print(f"Total time: {end - start:.2f} seconds")
    print("✅ Done. Results saved in outputs/sample_run.json")

def main():
    analyze_incidents()

if __name__ == "__main__":
    main()
    