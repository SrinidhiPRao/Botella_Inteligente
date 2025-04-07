import random
import time
import requests

# EC2_URL = "http://<YOUR_EC2_PUBLIC_IP>:8000/ingest"  # Replace with your EC2 IP
EC2_URL = "http://localhost:8000/ingest"  


def send_distance(distance: int):
    try:
        response = requests.post(EC2_URL, json={"distance": distance})
        print(f"Sent: {distance} | Response: {response.status_code}")
    except Exception as e:
        print(f"Failed to send: {e}")


def simulate_ultrasonic_data():
    """Simulates ultrasonic sensor readings and sends to EC2."""
    while True:
        distance = random.randint(10, 400)  # Simulated distance in cm
        send_distance(distance)
        time.sleep(1)  # Simulate a 1-second interval


if __name__ == "__main__":
    simulate_ultrasonic_data()
