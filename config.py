MONITORED_KEYS = [
r"Software\Microsoft\Windows\CurrentVersion\Run",
r"Software\Microsoft\Windows\CurrentVersion\RunOnce",
r"Software\Policies\Microsoft\Windows Defender",
r"Software\Microsoft\Windows\CurrentVersion\Policies\System",
r"Software\Microsoft\Windows NT\CurrentVersion\Winlogon"
]

HIVES = {"HKCU":"HKEY_CURRENT_USER","HKLM":"HKEY_LOCAL_MACHINE"}
POLL_INTERVAL = 5
