import json
import time
import winreg

import config
from analyzer import analyze_change
from detector import detect_changes
from logger import log_change


def get_values(hive, path):
    values = {}
    try:
        key = winreg.OpenKey(hive, path)
        index = 0
        while True:
            name, value, _ = winreg.EnumValue(key, index)
            values[name] = value
            index += 1
    except OSError:
        pass
    return values


def monitor(status_callback=None, log_callback=None, stop_event=None, baseline_path="baseline.json"):
    try:
        with open(baseline_path, "r", encoding="utf-8") as file:
            baseline = json.load(file)
    except FileNotFoundError:
        if status_callback:
            status_callback("Baseline not found. Please create baseline first.")
        return
    except Exception as exc:
        if status_callback:
            status_callback(f"Failed to load baseline: {exc}")
        return

    if status_callback:
        status_callback("Monitoring started.")

    while True:
        if stop_event and stop_event.is_set():
            if status_callback:
                status_callback("Monitoring stopped.")
            break

        for hive_name, hive in config.HIVES.items():
            hive_obj = getattr(winreg, hive)

            for path in config.MONITORED_KEYS:
                full_path = f"{hive_name}\\{path}"
                current_values = get_values(hive_obj, path)
                old_values = baseline.get(full_path, {})
                changes = detect_changes(old_values, current_values)

                for action, key, old_val, new_val in changes:
                    severity, reason = analyze_change(full_path, key, new_val)
                    message = f"[{severity}] {action} -> {full_path} -> {key}"

                    if status_callback:
                        status_callback(message)

                    log_change(
                        action,
                        full_path,
                        key,
                        old_val,
                        new_val,
                        severity,
                        reason,
                        callback=log_callback,
                    )

                baseline[full_path] = current_values

        with open(baseline_path, "w", encoding="utf-8") as file:
            json.dump(baseline, file, indent=4)

        time.sleep(config.POLL_INTERVAL)
