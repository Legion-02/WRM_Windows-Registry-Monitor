# 🔐 Advanced Windows Registry Monitoring Tool

## 📌 Overview
The **Advanced Windows Registry Monitoring Tool** is a Python-based security project designed to monitor and detect changes in the Windows Registry in real time. This project is built with a focus on **Blue Team / SOC (Security Operations Center)** use cases, helping identify unauthorized or suspicious modifications.

---

## 🎯 Objective
To detect and log changes in critical Windows Registry keys by comparing the current state with a predefined baseline, enabling early detection of potential security threats.

---

## 🚀 Features
- 🔍 Real-time registry monitoring  
- 📊 Baseline creation and comparison  
- ⚠️ Detection of:
  - Added keys  
  - Modified values  
  - Deleted entries  
- 📝 Automatic logging of changes (`logs.txt`)  
- ⚡ Lightweight and efficient Python implementation  

---

## 🛠️ Tech Stack
- Python  
- `winreg` (Windows Registry access)  
- JSON (baseline storage)  
- File handling (logging system)  

---

## 📂 Project Structure
```
├── main.py              # Entry point of the application
├── monitor.py           # Core monitoring logic
├── detector.py          # Change detection logic
├── baseline.py          # Baseline creation
├── config.py            # Configuration settings
├── baseline.json        # Stored baseline data
├── logs.txt             # Output logs (generated during runtime)
```

---

## ⚙️ How It Works
1. The system first creates a **baseline snapshot** of registry keys.
2. The monitoring module continuously checks for changes.
3. Any differences between the current state and baseline are:
   - Detected
   - Classified
   - Logged into `logs.txt`

---

## ▶️ How to Run
### Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/Advanced-Windows-Registry-Monitor.git
cd Advanced-Windows-Registry-Monitor
```

### Step 2: Run the project
```bash
python main.py
```

---

## 📸 Sample Output
```
[ALERT] Registry Key Modified:
Path: HKEY_LOCAL_MACHINE\Software\Example
Old Value: 0
New Value: 1
```

---

## 🔐 Use Case (SOC Perspective)
- Detect persistence mechanisms (e.g., autorun registry keys)
- Identify malware behavior
- Monitor unauthorized system changes
- Assist in incident response

---

## ⚠️ Requirements
- Windows OS  
- Python 3.x  
- Administrator privileges (recommended for full access)

---

## 📈 Future Enhancements
- Email/Slack alert integration  
- GUI dashboard  
- Threat intelligence integration  
- Advanced filtering for critical keys  

---

## 👨‍💻 Author
- Anush

---

## 📜 License
This project is for educational and security research purposes.
