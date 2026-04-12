

def main():
    print("🚀 AI Incident Explainer starting...")
    from utils import load_json
    incidents = load_json('data/incident_logs.json')
    print(f"Loaded {len(incidents)} incidents.")
    
    results = [] 
    for i in incidents:
        print(f"Processing incident: {i['id']}")
        from processor import process_incident 
        results.append(process_incident(i))

    from utils import save_json
    save_json(results, 'outputs/sample_run.json')
    
    print("✅ Done. Results saved in outputs/sample_run.json")

if __name__ == "__main__":
    main()
    