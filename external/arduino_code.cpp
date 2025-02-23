long duration; // Variable to store time taken to the pulse to reach
int distance;  // Variable to store distance calculated using  formula
int trigPin = 13;
int echoPin = 11;
int led = 9;
int buzzer = 10;
int sensorpin = A0;
int sensorpower = 5;
int led2 = 3;
void setup()
{
    pinMode(sensorpower, OUTPUT);
    pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
    pinMode(echoPin, INPUT);  // Sets the echoPin as an INPUT
    Serial.begin(9600);
    Serial.println("Distance measurement using Arduino Uno.");
    delay(500);
}
void loop()
{
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);        // wait for 2 ms to avoid collision in serial monitor
    digitalWrite(trigPin, HIGH); // turn on the Trigger to generate pulse
    delayMicroseconds(10);       // keep the trigger "ON" for 10 ms to generate pulse for 10
    digitalWrite(trigPin, LOW);  // Turn off the pulse trigger to stop pulse generation
    duration = pulseIn(echoPin, HIGH);
    distance = duration * 0.0344 / 2; // Expression to calculate distance using time
    Serial.print("Distance: ");
    Serial.print(distance); // Print the output in serial monitor
    Serial.println(" cm");
    if (distance > 10)
    {
        digitalWrite(led, HIGH);
        tone(buzzer, 1000, 500);
    }
    else
    {
        digitalWrite(led, LOW);
        noTone(buzzer);
    }
    delay(1000);
    digitalWrite(sensorpower, HIGH);
    delay(10);
    int watersensor = analogRead(sensorpin);
    digitalWrite(sensorpower, LOW);
    Serial.print("Water sensor: ");
    Serial.println(watersensor);
    if (watersensor > 350)
    {
        digitalWrite(led2, HIGH);
    }
    else
    {
        digitalWrite(led2, LOW);
    }
}