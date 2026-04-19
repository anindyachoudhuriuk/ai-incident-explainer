import json
from pathlib import Path
from datetime import datetime

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