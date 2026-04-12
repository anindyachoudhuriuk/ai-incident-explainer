

def load_json(file_path):
    import json
    with open(file_path, 'r') as path:
        return json.load(path)
    
def save_json(data, file_path):
    import json
    with open(file_path, 'a') as path:
        json.dump(data, path, indent=4)