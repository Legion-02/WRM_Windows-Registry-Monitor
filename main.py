import os
import config

from baseline import create_baseline
from monitor import monitor


def main():
    print("🔐 Windows Registry Monitoring System\n")

    # ✅ Check if baseline exists
    if not os.path.exists("baseline.json"):
        print("⚠️ Baseline not found. Creating new baseline...\n")
        create_baseline(config)
    else:
        print("✅ Baseline already exists.\n")

    print("🚀 Starting Advanced Registry Monitor...\n")

    try:
        monitor()
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user.")
    except Exception as e:
        print(f"❌ Error occurred: {e}")


if __name__ == "__main__":
    main()
