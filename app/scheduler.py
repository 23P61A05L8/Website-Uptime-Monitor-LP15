from apscheduler.schedulers.background import BackgroundScheduler
from app.monitor import check_website
from app.root_cause import get_root_cause_hint
from app.database import insert_check
from app.alert import send_down_alert

WEBSITES = [
    "https://google.com",
    "https://github.com",
    "http://119.235.51.91/ecap/",
    "https://www.vbithydexams.in/",
    "http://this-site-will-fail-12345.com",
]

_scheduler = None  # keep global reference

def monitor_job():
    print(">>> Scheduler running a check cycle")
    for url in WEBSITES:
        result = check_website(url)
        hint = get_root_cause_hint(result["error"])

        insert_check(
            url=url,
            status=result["status"],
            response_time=result["response_time"],
            error=result["error"],
            hint=hint
        )

        # 🔔 DOWN ALERT
        if result["status"] == "DOWN":
            send_down_alert(url, result["status"], hint)

        print(f"[CHECK] {url} -> {result['status']} | {hint}")

def start_scheduler():
    global _scheduler
    if _scheduler is None:
        _scheduler = BackgroundScheduler(daemon=True)
        _scheduler.add_job(monitor_job, "interval", seconds=60, id="uptime_job", replace_existing=True)
        _scheduler.start()
        print(">>> Scheduler started")
        monitor_job()  # immediate first run