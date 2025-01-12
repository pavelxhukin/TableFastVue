import pika

MQ_EXCHANGE = ""
MQ_ROUTING_KEY = "keyQueue"

RMQ_HOST = "localhost"
RMQ_PORT = 5672

RMQ_USER = "guest"
RMQ_PASSWORD = "guest"

connection_params = pika.ConnectionParameters(
    host=RMQ_HOST,
    port=RMQ_PORT,
    credentials=pika.PlainCredentials(RMQ_USER, RMQ_PASSWORD),
)

def send_rmq(message: str):
    connection = pika.BlockingConnection(connection_params)

    channel = connection.channel()

    channel.queue_declare(queue=MQ_ROUTING_KEY)

    channel.basic_publish(MQ_EXCHANGE,
                        MQ_ROUTING_KEY,
                        body=message)
    print(" [x] Sent 'Hello World!14531b'")

    connection.close()
