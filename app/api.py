from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import conn, cur
from datetime import datetime

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/data")
def get_data():
    """Fetches ultrasonic sensor data from SQLite and returns it as JSON."""
    cur.execute("SELECT time, distance FROM ultrasonic_data ORDER BY time DESC LIMIT 50;")
    results = cur.fetchall()

    if not results:
        return {"message": "No data available"}

    timestamps = list(reversed([row[0] for row in results]))
    distances = list(reversed([row[1] for row in results]))

    return {
        "labels": timestamps,
        "datasets": [
            {
                "label": "Ultrasonic Distance (cm)",
                "data": distances,
                "borderColor": "blue",
                "fill": False,
            }
        ],
    }
