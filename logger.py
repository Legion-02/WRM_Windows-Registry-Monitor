from datetime import datetime

def log_change(action, path, key, old, new):
    with open("logs.txt", "a") as f:
        f.write(f"\n[{datetime.now()}]\n")
        f.write(f"Action: {action}\n")
        f.write(f"Path: {path}\n")
        f.write(f"Key: {key}\n")
        f.write(f"Old Value: {old}\n")
        f.write(f"New Value: {new}\n")
        f.write("-------------------------\n")
