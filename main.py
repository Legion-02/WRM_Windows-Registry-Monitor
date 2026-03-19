from monitor import monitor
from baseline import create_baseline
import os, config

if not os.path.exists("baseline.json"):
    create_baseline(config)

print("Starting Advanced Registry Monitor...")
monitor()
