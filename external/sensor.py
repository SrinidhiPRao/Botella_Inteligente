import serial  # type: ignore
import time
from fastapi import FastAPI  # type: ignore
from fastapi.responses import StreamingResponse # type: ignore

app = FastAPI()

# Initialize serial connection
arduino = serial.Serial('COM5', 9600)
time.sleep(2)  # Allow Arduino to initialize

def read_ultrasonic_data():
    """Generator function to read distance data from Arduino via serial."""
    while True:
        if arduino.in_waiting > 0:
            data = arduino.readline().decode('utf-8').strip()
            if "Distance:" in data:
                distance = int(data.split(" ")[1])
                yield f"data: {distance}\n\n"  # SSE format

@app.get("/stream")
def stream_data():
    """Endpoint that streams ultrasonic sensor data via SSE."""
    return StreamingResponse(read_ultrasonic_data(), media_type="text/event-stream")

@app.on_event("shutdown")
def shutdown():
    """Close serial connection on server shutdown."""
    arduino.close()
