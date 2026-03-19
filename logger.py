import time
import json
import winreg
import config

from detector import detect_changes
from analyzer import analyze_change
from logger import log_change


# 🔹 Get registry values
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
    # ✅ Load baseline
    try:
        with open("baseline.json", "r") as f:
            baseline = json.load(f)
        print("✅ Baseline loaded successfully")
    except:
        print("❌ Failed to load baseline. Run baseline creation first.")
        return

    print("🔍 Monitoring started...\n")

    while True:
        for hive_name, hive in config.HIVES.items():
            hive_obj = getattr(winreg, hive)

            for path in config.MONITORED_KEYS:
                full_path = f"{hive_name}\\{path}"

                # 🔹 Get current values
                current_values = get_values(hive_obj, path)

                # 🔹 Get old values from baseline
                old_values = baseline.get(full_path, {})

                # 🔹 Detect changes
                changes = detect_changes(old_values, current_values)

                # 🔹 Process changes
                for change in changes:
                    action, key, old_val, new_val = change

                    severity, reason = analyze_change(
                        full_path, key, new_val
                    )

                    print(f"[{severity}] {action} → {full_path} → {key}")
                    print(f"Reason: {reason}\n")

                    log_change(
                        action,
                        full_path,
                        key,
                        old_val,
                        new_val,
                        severity,
                        reason
                    )

                # ✅ Update baseline in memory
                baseline[full_path] = current_values

        # 🔁 Debug indicator (VERY IMPORTANT)
        print("⏳ Monitoring cycle complete...\n")

        # ⏱ Wait before next scan
        time.sleep(config.POLL_INTERVAL)
