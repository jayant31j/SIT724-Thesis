import pika

# RabbitMQ connection parameters
amqp_host = 'localhost'  # Replace if RabbitMQ is on a different host
queue_name = 'sensor_queue'

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=amqp_host))
channel = connection.channel()

# Ensure the queue exists
channel.queue_declare(queue=queue_name)

# Callback function to process messages
def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode('utf-8')}")

# Set up consumer to listen to the specified queue
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
