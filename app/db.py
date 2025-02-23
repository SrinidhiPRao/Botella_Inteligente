import psycopg2  # type: ignore
import time

# Database connection details
DB_CONFIG = {
    "dbname": "waterlogdb",
    "user": "postgres",
    "password": "password",
    "host": "db",  # Use Docker service name
    "port": "5432",
}


# Function to connect to TimescaleDB with retry logic
def connect_db():
    while True:
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            print("✅ Connected to TimescaleDB!")
            return conn
        except psycopg2.OperationalError:
            print("⏳ Database not ready, retrying in 5 seconds...")
            time.sleep(5)


# Connect to the database
conn = connect_db()
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
