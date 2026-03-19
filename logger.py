from datetime import datetime
def log_change(a,p,k,o,n,s,r):
    with open("logs.txt","a") as f:
        f.write(f"[{datetime.now()}]\n{a} {p} {k}\nSeverity:{s}\nReason:{r}\n\n")
