from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from db import conn, cur
from datetime import datetime

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ingest")
async def ingest_data(request: Request):
    """Receives sensor data from remote device and stores it in SQLite."""
    try:
        body = await request.json()
        distance = int(body["distance"])
        cur.execute("INSERT INTO ultrasonic_data (distance) VALUES (?);", (distance,))
        conn.commit()
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "detail": str(e)}

@app.get("/data")
def get_data():
    """Fetches ultrasonic sensor data from SQLite."""
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
