def detect_changes(old, new):
    changes = []

    old_keys = set(old.keys())
    new_keys = set(new.keys())

    for key in new_keys - old_keys:
        changes.append(("ADDED", key, None, new[key]))

    for key in old_keys - new_keys:
        changes.append(("REMOVED", key, old[key], None))

    for key in old_keys & new_keys:
        if old[key] != new[key]:
            changes.append(("MODIFIED", key, old[key], new[key]))

    return changes
