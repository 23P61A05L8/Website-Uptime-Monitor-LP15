import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# 🔐 Set these as environment variables in Docker (recommended)
EMAIL_USER = os.getenv("ALERT_EMAIL_USER")       # your Gmail
EMAIL_PASS = os.getenv("ALERT_EMAIL_PASS")       # app password
ALERT_TO   = os.getenv("ALERT_EMAIL_TO")         # receiver email

def send_down_alert(url, status, hint):
    subject = "🚨 Website DOWN Alert"
    body = f"""
ALERT: Website is DOWN

URL: {url}
Status: {status}
Hint: {hint}

Time: This check was performed by Intelligent Website Uptime Monitor.
"""

    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER
    msg["To"] = ALERT_TO
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)
        print(f"📧 Email alert sent for {url}")
    except Exception as e:
        print(f"❌ Failed to send email alert: {e}")