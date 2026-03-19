import time
import json
import winreg
import config

from detector import detect_changes
from analyzer import analyze_change
from logger import log_change


def get_vals(h, p):
    vals = {}
    try:
        key = winreg.OpenKey(h, p)
        i = 0
        while True:
            name, value, _ = winreg.EnumValue(key, i)
            vals[name] = value
            i += 1
    except:
        pass
    return vals


def monitor():
    # ✅ Load baseline properly
    with open("baseline.json", "r") as f:
        baseline = json.load(f)

    print("✅ Baseline loaded successfully")

    while True:
        for hive_name, hive in config.HIVES.items():
            hive_obj = getattr(winreg, hive)

            for path in config.MONITORED_KEYS:
                full_path = f"{hive_name}\\{path}"

                current = get_vals(hive_obj, path)
                old = baseline.get(full_path, {})

                changes = detect_changes(old, current)

                for change in changes:
                    action, key, old_val, new_val = change

                    severity, reason = analyze_change(full_path, key, new_val)

                    print(f"[{severity}] {action} {full_path} → {key} ({reason})")

                    log_change(
                        action,
                        full_path,
                        key,
                        old_val,
                        new_val,
                        severity,
                        reason
                    )

                # ✅ update baseline in memory
                baseline[full_path] = current

        # ✅ wait before next scan
        time.sleep(config.POLL_INTERVAL)
