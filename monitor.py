import time
import json
import winreg
from detector import detect_changes
from logger import log_change
import config

def get_values(hive, path):
    values = {}
    try:
        key = winreg.OpenKey(hive, path)
        i = 0
        while True:
            name, value, _ = winreg.EnumValue(key, i)
            values[name] = value
            i += 1
    except OSError:
        pass
    return values

def monitor():
    with open("baseline.json", "r") as f:
        baseline = json.load(f)

    while True:
        for hive_name, hive in config.HIVES.items():
            hive_obj = getattr(winreg, hive)

            for path in config.MONITORED_KEYS:
                full_path = f"{hive_name}\\{path}"

                current = get_values(hive_obj, path)
                old = baseline.get(full_path, {})

                changes = detect_changes(old, current)

                for change in changes:
                    action, key, old_val, new_val = change
                    print(f"[ALERT] {action} in {full_path} -> {key}")
                    log_change(action, full_path, key, old_val, new_val)

                baseline[full_path] = current

        time.sleep(config.POLL_INTERVAL)
