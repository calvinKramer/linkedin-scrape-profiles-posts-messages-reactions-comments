thonimport json

def save_data_to_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def load_data_from_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)