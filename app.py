from flask import Flask, render_template_string
import subprocess

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Linux System Monitor</title>
    <style>
        body {
            font-family: Arial;
            background: #f4f4f4;
            text-align: center;
        }
        .container {
            width: 80%;
            margin: 40px auto;
        }
        .card {
            background: white;
            padding: 20px;
            margin: 15px;
            border-radius: 10px;
            box-shadow: 0 2px 8px #aaa;
        }
        h1 { color: #222; }
        pre { text-align: left; }
    </style>
</head>
<body>
<div class="container">
    <h1>🐧 Linux System Monitor</h1>

    <div class="card">
        <h2>CPU Usage</h2>
        <pre>{{ cpu }}</pre>
    </div>

    <div class="card">
        <h2>Memory Usage</h2>
        <pre>{{ memory }}</pre>
    </div>

    <div class="card">
        <h2>Disk Usage</h2>
        <pre>{{ disk }}</pre>
    </div>

    <div class="card">
        <h2>System Uptime</h2>
        <pre>{{ uptime }}</pre>
    </div>
</div>
</body>
</html>
"""

def command(cmd):
    return subprocess.getoutput(cmd)

@app.route("/")
def home():
    return render_template_string(
        HTML,
        cpu=command("top -bn1 | grep 'Cpu(s)'"),
        memory=command("free -h"),
        disk=command("df -h /"),
        uptime=command("uptime")
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
