from datetime import datetime
import os

def log_change(action, path, key, old, new, severity, reason):
    log_file = "logs.txt"

    try:
        with open(log_file, "a") as f:
            f.write(f"\n[{datetime.now()}]\n")
            f.write(f"Action: {action}\n")
            f.write(f"Path: {path}\n")
            f.write(f"Key: {key}\n")
            f.write(f"Old Value: {old}\n")
            f.write(f"New Value: {new}\n")
            f.write(f"Severity: {severity}\n")
            f.write(f"Reason: {reason}\n")
            f.write("-" * 40 + "\n")

        print("📝 Logged successfully")

    except Exception as e:
        print("❌ Logging failed:", e)
