import winreg
import json

def get_registry_values(hive, path):
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

def create_baseline(config):
    baseline = {}

    for hive_name, hive in config.HIVES.items():
        hive_obj = getattr(winreg, hive)

        for path in config.MONITORED_KEYS:
            full_path = f"{hive_name}\\{path}"
            values = get_registry_values(hive_obj, path)
            baseline[full_path] = values

    with open("baseline.json", "w") as f:
        json.dump(baseline, f, indent=4)

    print("Baseline created!")
