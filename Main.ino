#include "Arduino_SensorKit.h"

#define TRIGGER_PIN 7 // Ultrasonic sensor trigger pin
#define ECHO_PIN 8    // Ultrasonic sensor echo pin

void setup() {
  Serial.begin(9600); 
  while (!Serial);    
  pinMode(TRIGGER_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  Oled.begin();
  Oled.setFlipMode(true);
  Accelerometer.begin();
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

  // Display collected data on OLED
  Oled.clearDisplay();
  Oled.setFont(u8x8_font_chroma48medium8_r);
  Oled.setCursor(0, 3);
  Oled.print("x:");
  Oled.print(accelerationX, 2); 
  Oled.print(", y:");
  Oled.print(accelerationY, 2); 
  Oled.print(", z:");
  Oled.println(accelerationZ, 2); 
  Oled.setCursor(0, 4);
  Oled.print("Ultrasonic:");
  Oled.print(distance);
  Oled.setCursor(0, 5);
  Oled.print("Temp:");
  Oled.print(temp);
  Oled.setCursor(0, 6);
  Oled.print("Humidity:");
  Oled.print(humidity);

  // Print collected data to serial monitor
  Serial.println("------- Sensor Readings -------");
  Serial.print("x:");
  Serial.print(accelerationX, 2); 
  Serial.print(", y:");
  Serial.print(accelerationY, 2); 
  Serial.print(", z:");
  Serial.println(accelerationZ, 2); 
  Serial.print("Ultrasonic Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.println(" °C");
  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");
  Serial.println("-------------------------------");

  delay(1000); 
}
