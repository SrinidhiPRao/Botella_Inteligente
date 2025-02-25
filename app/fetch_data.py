import requests  # type: ignore
from db import conn, cur  # Import database connection

FASTAPI_URL = "http://host.docker.internal:5000/stream"


def fetch_and_store_data():
    """Fetches data from FastAPI and inserts into TimescaleDB."""
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


if __name__ == "__main__":
    fetch_and_store_data()
