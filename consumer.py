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



connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue=MQ_ROUTING_KEY)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(MQ_ROUTING_KEY, 
                      callback, 
                      auto_ack=True)

channel.start_consuming()