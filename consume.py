# consume.py
import pika, os
from typing import TypedDict

class ItemDto(TypedDict):
    count: int
    message: str


# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://sorin:sorin@localhost:5672')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
def callback(ch, method, properties, body):
  data = eval(body)
  item: ItemDto = data
  print(" [x] Received " + str(item))

  with open("consumer_message.txt", 'w') as f:
     f.write(item['message'])


channel.basic_consume('hello',
                      callback,
                      auto_ack=True)

print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()