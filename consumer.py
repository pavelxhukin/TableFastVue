import pika

from config import (
    get_connection,
    MQ_ROUTING_KEY,
)


connection = pika.BlockingConnection(get_connection())

channel = connection.channel()

channel.queue_declare(queue=MQ_ROUTING_KEY)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(MQ_ROUTING_KEY, 
                      callback, 
                      auto_ack=True)

channel.start_consuming()