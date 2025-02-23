import requests  # type:ignore
import psycopg2  # type: ignore
import time

# Database connection details (matches docker-compose.yml)
DB_CONFIG = {
    "dbname": "waterlogdb",
    "user": "postgres",
    "password": "password",
    "host": "db",  # Use the service name from docker-compose
    "port": "5432",
}

# FastAPI server URL (outside container)
FASTAPI_URL = "http://host.docker.internal:5000/stream"
# FASTAPI_URL = "http://127.0.0.1:5000/stream"

# Connect to TimescaleDB
while True:
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("✅ Connected to TimescaleDB!")
        break
    except psycopg2.OperationalError:
        print("⏳ Database not ready, retrying in 5 seconds...")
        time.sleep(5)
cur = conn.cursor()

# Create a hypertable for time-series data
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS ultrasonic_data (
        time TIMESTAMPTZ DEFAULT NOW(),
        distance INT
    );
"""
)
cur.execute(
    "SELECT create_hypertable('ultrasonic_data', 'time', if_not_exists => TRUE);"
)
conn.commit()

# Read data from FastAPI and insert into TimescaleDB
with requests.get(FASTAPI_URL, stream=True) as response:
    for line in response.iter_lines():
        if line and line.startswith(b"data:"):
            distance = int(line.decode().split(": ")[1])
            print(f"Storing Distance: {distance}")

            # Insert data into TimescaleDB
            cur.execute(
                "INSERT INTO ultrasonic_data (distance) VALUES (%s)", (distance,)
            )
            conn.commit()
