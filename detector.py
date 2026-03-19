def detect_changes(old,new):
    changes=[]
    ok=set(old.keys()); nk=set(new.keys())
    for k in nk-ok: changes.append(("ADDED",k,None,new[k]))
    for k in ok-nk: changes.append(("REMOVED",k,old[k],None))
    for k in ok&nk:
        if old[k]!=new[k]: changes.append(("MODIFIED",k,old[k],new[k]))
    return changes
