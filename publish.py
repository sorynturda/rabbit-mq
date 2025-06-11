# publish.py
import pika, os
from typing import TypedDict
from random import randint
from pypdf import PdfReader

class ItemDto(TypedDict):
    count: int
    message: str

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://sorin:sorin@localhost:5672')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue

reader = PdfReader('ps_rezumat.pdf')
page=reader.pages[0]

itemDto = ItemDto(
    count=randint(1,1000),
    message=page.extract_text()
)

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=str(itemDto))

print(f" [x] Sent: {itemDto}")
connection.close()