import config
from baseline import create_baseline
from monitor import monitor
import os

if not os.path.exists("baseline.json"):
    create_baseline(config)

print("Starting Registry Monitor...")
monitor()
