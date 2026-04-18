from pathlib import Path
import time
from utils import save_json
from utils import load_json
from processor import process_incident 

def main():
    print("🚀 AI Incident Explainer starting...")
    start = time.time()
    ROOT = Path(__file__).resolve().parent.parent
    incidents = load_json(ROOT / "data" / "incident_logs.json")
    print(f"Loaded {len(incidents)} incidents.")
    
    results = [] 
    
    for i in incidents:
        print(f"Processing incident: {i['id']}")
        results.append(process_incident(i))

    save_json(results, ROOT / "outputs" / "sample_run.json")
    end = time.time()
    print(f"Total time: {end - start:.2f} seconds")
    print("✅ Done. Results saved in outputs/sample_run.json")

if __name__ == "__main__":
    main()
    