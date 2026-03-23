from flask import Flask, render_template
from app.database import init_db, get_latest_checks, get_uptime_percentage
from app.scheduler import start_scheduler

app = Flask(__name__)

@app.route("/")
def dashboard():
    history = get_latest_checks(20)
    uptime_stats = get_uptime_percentage()
    return render_template("dashboard.html", history=history, uptime_stats=uptime_stats)

if __name__ == "__main__":
    init_db()
    start_scheduler()
    app.run(host="0.0.0.0", port=5000, debug=False)