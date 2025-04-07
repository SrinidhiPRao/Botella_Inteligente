import serial  # type: ignore
import time
import requests

# Arduino serial port
arduino = serial.Serial('COM5', 9600)
time.sleep(2)  # Wait for Arduino to initialize

EC2_URL = "http://<YOUR_EC2_PUBLIC_IP>:8000/ingest"  # Replace with your EC2 IP

def send_distance(distance: int):
    try:
        response = requests.post(EC2_URL, json={"distance": distance})
        print(f"Sent: {distance} | Response: {response.status_code}")
    except Exception as e:
        print(f"Failed to send: {e}")

while True:
    if arduino.in_waiting > 0:
        data = arduino.readline().decode('utf-8').strip()
        if "Distance:" in data:
            try:
                distance = int(data.split(" ")[1])
                send_distance(distance)
            except ValueError:
                print(f"Invalid data: {data}")
