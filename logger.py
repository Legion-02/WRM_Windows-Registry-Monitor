from datetime import datetime

LOG_FILE = "logs.txt"


def format_log_entry(action, path, key, old, new, severity, reason):
    return (
        f"[{datetime.now():%Y-%m-%d %H:%M:%S}]\n"
        f"Action: {action}\n"
        f"Path: {path}\n"
        f"Key: {key}\n"
        f"Old Value: {old}\n"
        f"New Value: {new}\n"
        f"Severity: {severity}\n"
        f"Reason: {reason}\n"
        + ("-" * 50)
        + "\n"
    )


def log_change(action, path, key, old, new, severity, reason, callback=None):
    entry = format_log_entry(action, path, key, old, new, severity, reason)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(entry)

    if callback is not None:
        try:
            callback(entry)
        except Exception:
            pass

    return entry
