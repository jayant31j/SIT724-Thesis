import serial
import pika

# Configure the serial port (replace with your correct port)
serial_port = '/dev/cu.usbmodem144201'
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=1)

# RabbitMQ setup
amqp_host = 'localhost'  # Replace with your RabbitMQ broker's IP if needed
queue_name = 'sensor_queue'

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=amqp_host))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue=queue_name)

while True:
    # Read data from Arduino
    line = ser.readline().decode('utf-8').strip()
    if line:
        print(f"Received data: {line}")
        # Publish data to RabbitMQ
        channel.basic_publish(exchange='', routing_key=queue_name, body=line)
