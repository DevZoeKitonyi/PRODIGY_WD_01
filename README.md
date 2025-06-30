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
   ```python
   from flask import Flask, render_template_string, request
   from TimeKeeper import TimeKeeper

   app = Flask(__name__)
   stopwatch = TimeKeeper()

   HTML_TEMPLATE = """
   <!DOCTYPE html>
   <html>
   <head>
       <title>Python Stopwatch</title>
       <style>
           body { font-family: Arial; text-align: center; margin-top: 50px; }
           .time { font-size: 3em; margin: 20px; }
           button { padding: 10px 20px; font-size: 1em; margin: 5px; }
       </style>
   </head>
   <body>
       <h1>Python Stopwatch</h1>
       <div class="time">{{ time }}</div>
       <div>
           <a href="/start"><button>Start</button></a>
           <a href="/pause"><button>Pause</button></a>
           <a href="/resume"><button>Resume</button></a>
           <a href="/reset"><button>Reset</button></a>
           <a href="/lap"><button>Lap</button></a>
       </div>
       {% if laps %}
       <h3>Lap Times:</h3>
       <ul>
           {% for lap in laps %}
           <li>{{ lap }}</li>
           {% endfor %}
       </ul>
       {% endif %}
   </body>
   </html>
   """

   @app.route("/")
   def home():
       h, m, s = stopwatch.get_current_time()
       time_str = f"{int(h):02d}:{int(m):02d}:{int(s):02d}"
       return render_template_string(HTML_TEMPLATE, time=time_str, laps=stopwatch.laps)

   @app.route("/start")
   def start():
       stopwatch.start()
       return home()

   @app.route("/pause")
   def pause():
       stopwatch.pause()
       return home()

   @app.route("/resume")
   def resume():
       stopwatch.resume()
       return home()

   @app.route("/reset")
   def reset():
       stopwatch.reset()
       return home()

   @app.route("/lap")
   def lap():
       stopwatch.lap()
       return home()

   if __name__ == "__main__":
       app.run(debug=True)
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

---

## **🎮 Usage Instructions**
### **Command Line Version**
![CLI Demo](https://i.imgur.com/JQ8Z5lW.gif) *(Example GIF)*  
- Press `S` to start, `P` to pause.
- `L` records laps, `C` resets.

### **Web Version**
![Web Demo](https://i.imgur.com/9Xv7xT3.gif) *(Example GIF)*  
- Click buttons to control.
- Lap times appear below.

---

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

Would you like me to add **more features** like sound alerts or a countdown timer? 🚀