# 🛡️ Windows Registry Monitoring System (WRM) – GUI Version

A **GUI-based real-time Windows Registry Monitoring System** built using Python.  
This tool detects **unauthorized changes in registry keys** and simulates **SOC-level monitoring**.

---

## 🚀 Features

- ✅ Real-time registry monitoring  
- 🖥️ User-friendly GUI (Tkinter)  
- 📊 Live output display  
- 📁 Log file generation (`logs.txt`)  
- 🔍 Detects:
  - Added registry keys  
  - Modified values  
  - Deleted entries  
- ⚙️ Adjustable polling interval  
- ▶️ Start / Stop monitoring  

---

## 🧠 Why this Project?

The Windows Registry is commonly used by attackers for:

- Persistence mechanisms  
- Malware execution  
- System manipulation  

👉 This tool helps detect such behavior in real time.

---

## 🏗️ Project Structure

WRM_Windows-Registry-Monitor/

├── gui.py 
├── main.py 
├── monitor.py 
├── baseline.py 
├── detector.py 
├── analyzer.py 
├── logger.py 
├── config.py 
├── baseline.json 
├── logs.txt 
└── README.md 

---

## ⚙️ Installation

git clone https://github.com/your-username/WRM_Windows-Registry-Monitor.git  
cd WRM_Windows-Registry-Monitor

---

## ▶️ Run the Project

### GUI Version (Recommended)
python gui.py

### CLI Version
python main.py

---

## 🖥️ GUI Controls

- Create Baseline → Capture registry snapshot  
- Start Monitoring → Begin tracking changes  
- Stop Monitoring → Stop monitoring  
- Open Logs → View logs  
- Clear Screen → Reset output  

---

## 🔄 How It Works

1. Baseline is created (`baseline.json`)  
2. Registry is continuously monitored  
3. Changes are detected  
4. Output is:
   - Displayed in GUI  
   - Saved in `logs.txt`  

---

## 🧪 Example Log Output

[INFO] Registry Key Added: HKCU\Software\TestKey  
[WARNING] Registry Value Modified: HKLM\...\Run  
[ALERT] Registry Key Deleted: HKCU\Software\MaliciousKey  

---

## ⚠️ Important Notes

- Run as Administrator  
- Works only on Windows OS  
- For educational purposes only  

---

## 📈 Future Improvements

- Alerts (Email / Telegram)  
- Dashboard view  
- SIEM integration  
- ML-based detection  

---

## 👨‍💻 Author

Anush P  
Cybersecurity Enthusiast  

---

