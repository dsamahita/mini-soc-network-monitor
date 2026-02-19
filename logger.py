import sqlite3
from datetime import datetime

DB_NAME = "database.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            reason TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()

def log_suspicious(ip, reason):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO logs (ip, reason, timestamp)
        VALUES (?, ?, ?)
    """, (ip, reason, datetime.now()))

    conn.commit()
    conn.close()
