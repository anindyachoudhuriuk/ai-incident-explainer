from pathlib import Path

from config.config_loader import load_config
from utils.utils import load_json, save_versioned_leaderboard, ensure_model_ready
from llms.processor import process_incident 
import time

def run_evaluation():
    print("🚀 Starting evaluation...")

    config = load_config()
    models = config.models

    ROOT = Path(__file__).resolve().parent.parent
    incidents = load_json(ROOT / "data" / "incident_logs.json")

    print(f"Loaded {len(incidents)} incidents.")

    results = []

    for model in models:
        if not ensure_model_ready(model):
            continue

        print(f"Evaluating model: {model}")

        final_scores = 0.0
        start = time.time()

        for i in incidents:
            print(f"Processing incident: {i['id']}")

            # Step 1: LLM processing
            result = process_incident(i, model)

            # Step 2: Evaluate
            metrics = evaluate_output(result)

            # Step 3: Score
            final_scores += compute_final_score(metrics)

        avg_score = final_scores / len(incidents)

        results.append({
            "evaluation": {
                "model": model,
                "final_score": avg_score
            }
        })

        print(f"Model {model} score: {avg_score}")

    # ✅ FIX: sort AFTER loop ends
    results.sort(
        key=lambda x: x["evaluation"]["final_score"],
        reverse=True
    )

    leaderboard = {
        "models": results,
        "best_model": results[0]["evaluation"]["model"]
    }

    save_versioned_leaderboard(leaderboard, ROOT  )

    end = time.time()
    print(f"Total time: {end - start:.2f} seconds")
    print("✅ Done.")
    
from pathlib import Path
import json


    
def main():
    run_evaluation()

if __name__ == "__main__":
    main()