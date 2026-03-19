def analyze_change(path,key,value):
    p=path.lower(); k=str(key).lower(); v=str(value).lower()
    if "run" in p: return "HIGH","Persistence detected"
    if "defender" in p: return "CRITICAL","Defender tampering"
    if "enablelua" in k and str(value)=="0": return "CRITICAL","UAC disabled"
    if "winlogon" in p and k=="shell": return "CRITICAL","Shell hijack"
    return "LOW","Normal change"
