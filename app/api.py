from fastapi import FastAPI  # type:ignore
from fastapi.middleware.cors import CORSMiddleware  # type:ignore
from db import conn, cur  # Import database connection

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
    """Fetches ultrasonic sensor data from TimescaleDB and returns it as JSON."""
    cur.execute(
        "SELECT time, distance FROM ultrasonic_data ORDER BY time ASC LIMIT 50;"
    )
    results = cur.fetchall()

    if not results:
        return {"message": "No data available"}

    timestamps = [row[0].isoformat() for row in results]  # Convert timestamps to string
    distances = [row[1] for row in results]  # Extract distance values

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
