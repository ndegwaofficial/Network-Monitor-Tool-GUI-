from flask import Flask, render_template
from network_monitor import NetworkMonitor

app = Flask(__name__)
monitor = NetworkMonitor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start_monitoring():
    monitor.discover_devices()
    monitor.start_monitoring()
    return "Monitoring started!"

if __name__ == "__main__":
    app.run(debug=True)
