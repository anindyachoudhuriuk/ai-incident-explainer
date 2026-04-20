import json
from pathlib import Path
from datetime import datetime
import time, subprocess 

def load_json(file_path):
    import json
    with open(file_path, 'r') as path:
        return json.load(path)
    
def save_json(data, file_path):
    import json
    with open(file_path, 'a') as path:
        json.dump(data, path, indent=4)
        
def save_versioned_leaderboard(leaderboard, root: Path):
    output_dir = root / "outputs" / "leaderboards"
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")

    versioned_path = output_dir / f"leaderboard_{timestamp}.json"
    latest_path = output_dir / "latest.json"

    # Save versioned copy
    with open(versioned_path, "w", encoding="utf-8") as f:
        json.dump(leaderboard, f, indent=2)

    # Overwrite latest
    with open(latest_path, "w", encoding="utf-8") as f:
        json.dump(leaderboard, f, indent=2)

    return versioned_path

def load_latest_leaderboard(root: Path):
    path = root / "outputs" / "leaderboards" / "latest.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def ensure_model_ready(model_name: str):
    if is_model_available(model_name):
        return True

    print(f"\n⚠️ Model '{model_name}' is not ready or loaded.")
    choice = input("Start model now? (y/n): ").strip().lower()

    if choice == "y":
        print(f"🚀 Please run in another terminal:\n  ollama run {model_name}\n")
        wait_for_model(model_name)
        return True

    print("❌ Skipping model.")
    return False


def wait_for_model(model_name: str, timeout=60):
    start = time.time()

    while time.time() - start < timeout:
        if is_model_available(model_name):
            print(f"✅ Model ready: {model_name}")
            return True

        print(f"⏳ Waiting for model: {model_name}...")
        time.sleep(2)

    return False

def is_model_available(model_name: str) -> bool:
    result = subprocess.run(
        ["ollama", "ps"],
        capture_output=True,
        text=True
    )
    return model_name in result.stdout