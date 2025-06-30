 Stopwatch Application - Comprehensive Guide**

---

## **📌 Table of Contents**
1. [Application Overview](#-application-overview)
2. [Features](#-features)
3. [How to Run](#-how-to-run)
   - [Command Line Version](#-command-line-version)
   - [Browser Version (Flask Web App)](#-browser-version-flask-web-app)
4. [File Structure](#-file-structure)
5. [Dependencies](#-dependencies)
6. [Usage Instructions](#-usage-instructions)
7. [Future Improvements](#-future-improvements)
8. [Troubleshooting](#-troubleshooting)

---

## **🌐 Application Overview**
This is a **Python-based Stopwatch** with two versions:
1. **Command Line Interface (CLI)** – Runs in terminal (`MainApp.py`).
2. **Web Browser Interface** – Runs on Flask (`WebApp.py`).
![Screenshot 2025-06-30 184419](https://github.com/user-attachments/assets/c93f42f0-53f5-43d4-80c2-fcf5be879428)
![Screenshot 2025-06-30 184403](https://github.com/user-attachments/assets/7b712145-cded-43f8-b4ae-4800e5bc89a5)
![Screenshot 2025-06-30 184432](https://github.com/user-attachments/assets/a7571b83-9d9e-4161-9713-0e0e4ec6d862)

The stopwatch supports:
- **Start, Pause, Resume, Reset**
- **Lap Time Recording**
- **Color-Coded Feedback (CLI)**
- **Real-Time Display (Web)**

---

## **✨ Features**
| Feature | CLI Version | Web Version |
|---------|------------|------------|
| Start/Pause/Resume | ✅ | ✅ |
| Reset Stopwatch | ✅ | ✅ |
| Lap Time Recording | ✅ | ✅ |
| Persistent Time Display | ✅ | ✅ |
| Colorful UI | ✅ | ❌ |
| Browser-Based | ❌ | ✅ |

---

## **🚀 How to Run**

### **🖥️ Command Line Version**
1. **Save the files** in a folder:
   - `TimeKeeper.py` (Core logic)
   - `StopwatchUI.py` (Terminal interface)
   - `MainApp.py` (Entry point)

2. **Run in terminal:**
   ```bash
   python MainApp.py
   ```
3. **Controls:**
   - `S` → Start  
   - `P` → Pause  
   - `R` → Resume  
   - `L` → Record Lap  
   - `C` → Reset  
   - `Q` → Quit  

### **🌐 Browser Version (Flask Web App)**
1. **Install Flask:**
   ```bash
   pip install flask
   ```
2. **Create `WebApp.py`:**

   ```
3. **Run the web app:**
   ```bash
   python WebApp.py
   ```
4. **Open in browser:**  
   Visit → [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## **📂 File Structure**
```
stopwatch-app/
│
├── TimeKeeper.py       # Core stopwatch logic
├── StopwatchUI.py      # Terminal interface
├── MainApp.py          # CLI entry point
├── WebApp.py           # Flask web version
└── README.md           # This guide
```

---

## **📦 Dependencies**
- **CLI Version:**  
  Only requires Python (3.6+).
  
- **Web Version:**  
  Requires:
  ```bash
  pip install flask
  ```





## **🔮 Future Improvements**
- [ ] **Save lap history** (CSV/JSON)
- [ ] **Graphical version (Tkinter/PyQt)**
- [ ] **Mobile-friendly web UI**
- [ ] **Countdown timer mode**

---

## **⚠️ Troubleshooting**
| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install flask` |
| Flask app not loading | Check if port 5000 is free |
| Time display glitch | Ensure `TimeKeeper.py` is in the same folder |

---

## **🎉 Conclusion**
Now you have **two versions** of the stopwatch:
1. **For terminal users** (`MainApp.py`)
2. **For web users** (`WebApp.py`)

