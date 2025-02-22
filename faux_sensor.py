import random
import time
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

def simulate_ultrasonic_data():
    """Generator that simulates ultrasonic sensor readings."""
    while True:
        distance = random.randint(10, 400)  # Simulating distances in cm
        yield f"data: {distance}\n\n"
        time.sleep(1)  # Simulating sensor reading every second

@app.get("/stream")
def stream_data():
    """Endpoint that streams fake ultrasonic sensor data via SSE."""
    return StreamingResponse(simulate_ultrasonic_data(), media_type="text/event-stream")

