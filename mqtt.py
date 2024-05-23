import serial
import paho.mqtt.client as mqtt

# Configure serial port (replace with your correct port)
serial_port = '/dev/cu.usbmodem144201'
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=1)

# MQTT broker configuration
broker_ip = 'localhost'  # Replace with your broker's IP
topic = 'sensor/gait'

# Initialize MQTT client
client = mqtt.Client()
client.connect(broker_ip, 1883, 60)

while True:
    # Read from Arduino
    line = ser.readline().decode('utf-8').strip()
    if line:
        print(f"Received data: {line}")
        client.publish(topic, line)
