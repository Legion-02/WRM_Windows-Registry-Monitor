import time, json, winreg, config
from detector import detect_changes
from analyzer import analyze_change
from logger import log_change

def get_vals(h,p):
    vals={}
    try:
        k=winreg.OpenKey(h,p); i=0
        while True:
            n,v,_=winreg.EnumValue(k,i); vals[n]=v; i+=1
    except: pass
    return vals

def monitor():
    baseline={}
    while True:
        for hn,h in config.HIVES.items():
            ho=getattr(winreg,h)
            for p in config.MONITORED_KEYS:
                fp=f"{hn}\\{p}"
                cur=get_vals(ho,p)
                old=baseline.get(fp,{})
                changes=detect_changes(old,cur)
                for c in changes:
                    a,k,o,n=c
                    s,r=analyze_change(fp,k,n)
                    print(f"[{s}] {a} {fp} {k}")
                    log_change(a,fp,k,o,n,s,r)
                baseline[fp]=cur
        time.sleep(config.POLL_INTERVAL)
