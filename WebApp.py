from flask import Flask, render_template_string, request
from Timekeeper import TimeKeeper
import time

app = Flask(__name__)
stopwatch = TimeKeeper()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Colorful Python Stopwatch</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            margin-top: 30px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 30px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            margin-bottom: 30px;
        }
        .time-display {
            font-size: 4em;
            font-weight: bold;
            margin: 30px 0;
            color: {{ time_color }};
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        .btn-group {
            margin: 25px 0;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
        }
        .btn {
            padding: 12px 25px;
            font-size: 1.1em;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s;
            font-weight: bold;
        }
        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .btn-start {
            background-color: #2ecc71;
            color: white;
        }
        .btn-pause {
            background-color: #e74c3c;
            color: white;
        }
        .btn-resume {
            background-color: #3498db;
            color: white;
        }
        .btn-reset {
            background-color: #f39c12;
            color: white;
        }
        .btn-lap {
            background-color: #9b59b6;
            color: white;
        }
        .lap-section {
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #eee;
        }
        .lap-title {
            color: #7f8c8d;
            margin-bottom: 15px;
        }
        .lap-list {
            list-style: none;
            padding: 0;
            max-height: 200px;
            overflow-y: auto;
        }
        .lap-item {
            padding: 10px;
            margin: 5px 0;
            background-color: #f8f9fa;
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
        }
        .lap-item:nth-child(odd) {
            background-color: #ecf0f1;
        }
        .status-message {
            margin: 15px 0;
            padding: 10px;
            border-radius: 5px;
            font-weight: bold;
        }
        .status-running {
            background-color: #d5f5e3;
            color: #27ae60;
        }
        .status-paused {
            background-color: #fadbd8;
            color: #e74c3c;
        }
        .status-reset {
            background-color: #fdebd0;
            color: #f39c12;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌈 Colorful Stopwatch</h1>
        
        {% if status_message %}
        <div class="status-message status-{{ status_type }}">
            {{ status_message }}
        </div>
        {% endif %}
        
        <div class="time-display">
            {{ time }}
        </div>
        
        <div class="btn-group">
            <a href="/start" class="btn btn-start">Start</a>
            <a href="/pause" class="btn btn-pause">Pause</a>
            <a href="/resume" class="btn btn-resume">Resume</a>
            <a href="/reset" class="btn btn-reset">Reset</a>
            <a href="/lap" class="btn btn-lap">Lap</a>
        </div>
        
        {% if laps %}
        <div class="lap-section">
            <h3 class="lap-title">⏱️ Lap Times</h3>
            <ul class="lap-list">
                {% for lap in laps %}
                <li class="lap-item">
                    <span>Lap {{ loop.index }}</span>
                    <span>{{ lap }}</span>
                </li>
                {% endfor %}
            </ul>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

def format_lap_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

@app.route("/")
def home():
    h, m, s = stopwatch.get_current_time()
    time_str = f"{int(h):02d}:{int(m):02d}:{int(s):02d}"
    
    # Dynamic time color based on state
    time_color = "#3498db"  # Default blue
    status_message = None
    status_type = None
    
    if stopwatch.running:
        time_color = "#2ecc71"  # Green when running
        status_message = "Stopwatch is running"
        status_type = "running"
    elif stopwatch.elapsed_time > 0:
        time_color = "#e74c3c"  # Red when paused
        status_message = "Stopwatch is paused"
        status_type = "paused"
    else:
        time_color = "#f39c12"  # Orange when reset
        status_message = "Stopwatch is ready"
        status_type = "reset"
    
    # Format lap times for display
    formatted_laps = [format_lap_time(lap) for lap in stopwatch.laps]
    
    return render_template_string(
        HTML_TEMPLATE,
        time=time_str,
        time_color=time_color,
        laps=formatted_laps,
        status_message=status_message,
        status_type=status_type
    )

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
    if stopwatch.running:
        stopwatch.lap()
    return home()

if __name__ == "__main__":
    app.run(debug=True)