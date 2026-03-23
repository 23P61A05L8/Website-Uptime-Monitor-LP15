import sqlite3
from datetime import datetime
import os

DB_PATH = os.path.join(os.getcwd(), "uptime.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS checks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            status TEXT,
            response_time REAL,
            error TEXT,
            hint TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_check(url, status, response_time, error, hint):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO checks (url, status, response_time, error, hint, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (url, status, response_time, error, hint, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def get_latest_checks(limit=20):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT url, status, response_time, error, hint, timestamp
        FROM checks
        ORDER BY id DESC
        LIMIT ?
    """, (limit,))
    rows = cur.fetchall()
    conn.close()
    return rows

# 📈 Uptime percentage per website
def get_uptime_percentage():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        SELECT url,
               ROUND(SUM(CASE WHEN status = 'UP' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS uptime_pct,
               COUNT(*) AS total_checks
        FROM checks
        GROUP BY url
        ORDER BY url
    """)
    rows = cur.fetchall()
    conn.close()
    return rows