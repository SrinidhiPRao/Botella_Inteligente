import sqlite3
from datetime import datetime
import time

# SQLite DB file
DB_FILE = "data/ultrasonic_data.db"

# Connect to SQLite (will create file if it doesn't exist)
def connect_db():
    while True:
        try:
            conn = sqlite3.connect(DB_FILE, check_same_thread=False)
            print("✅ Connected to SQLite!")
            return conn
        except sqlite3.OperationalError:
            print("⏳ SQLite DB not ready, retrying in 5 seconds...")
            time.sleep(5)

# Connect to the database
conn = connect_db()
cur = conn.cursor()

# Create table for ultrasonic data
cur.execute("""
    CREATE TABLE IF NOT EXISTS ultrasonic_data (
        time TEXT DEFAULT (DATETIME('now')),
        distance INTEGER
    );
""")
conn.commit()
