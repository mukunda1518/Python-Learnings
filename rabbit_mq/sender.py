import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
channel = connection.channel()


channel.queue_declare(queue="hello")

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(exchange="", routing_key="hello", body=message)

print(f" [x] Sent {message}")

connection.close()