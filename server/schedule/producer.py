import pika

from config import (
    get_connection,
    MQ_EXCHANGE,
    MQ_ROUTING_KEY,
)

def produce_message(message_body: str) -> None:
    connection = pika.BlockingConnection(get_connection())
    channel = connection.channel()
    channel.queue_declare(queue=MQ_ROUTING_KEY)
    channel.basic_publish(
        exchange=MQ_EXCHANGE,
        routing_key=MQ_ROUTING_KEY,
        body=message_body,
    )
    connection.close()