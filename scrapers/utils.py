import os

def save_raw_response(data, filename):
    os.makedirs("data/raw", exist_ok=True)
    path = f"data/raw/{filename}.json"
    with open(path, "w") as f:
        f.write(str(data))
    return path