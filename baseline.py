import json, winreg, config
def create_baseline(cfg):
    data={}
    for hn,h in cfg.HIVES.items():
        ho=getattr(winreg,h)
        for p in cfg.MONITORED_KEYS:
            data[f"{hn}\\{p}"]={}
    with open("baseline.json","w") as f:
        json.dump(data,f)
    print("Baseline created")
