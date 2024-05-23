#include "Arduino_SensorKit.h"

#define TRIGGER_PIN 7 // Ultrasonic sensor trigger pin
#define ECHO_PIN 8    // Ultrasonic sensor echo pin

void setup() {
  Serial.begin(9600);
  while (!Serial); // Wait for the serial port to connect
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  Oled.begin();
  Oled.setFlipMode(true);
  Accelerometer.begin();

  // Print a single header line at the start
  Serial.println("Timestamp,AccelerationX,AccelerationY,AccelerationZ,UltrasonicDistance,Temperature,Humidity");
}

void loop() {
  // Read accelerometer data
  float accelerationX = Accelerometer.readX();
  float accelerationY = Accelerometer.readY();
  float accelerationZ = Accelerometer.readZ();

  // Read ultrasonic sensor data
  long duration, distance;
  digitalWrite(TRIGGER_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIGGER_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER_PIN, LOW);
  duration = pulseIn(ECHO_PIN, HIGH);
  distance = duration * 0.034 / 2; // Convert duration to distance in cm

  // Read DHT22 sensor data
  float temp = Environment.readTemperature();
  float humidity = Environment.readHumidity();

  // Print data in CSV format
  Serial.print(millis());
  Serial.print(",");
  Serial.print(accelerationX, 2);
  Serial.print(",");
  Serial.print(accelerationY, 2);
  Serial.print(",");
  Serial.print(accelerationZ, 2);
  Serial.print(",");
  Serial.print(distance);
  Serial.print(",");
  Serial.print(temp, 2);
  Serial.print(",");
  Serial.println(humidity, 2);

  delay(1000); // Delay for 1 second before next read
}
