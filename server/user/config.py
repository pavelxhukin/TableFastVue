import pika
import aio_pika
import asyncio

RMQ_HOST = "rabbitmq"
RMQ_PORT = 5672

RMQ_USER = "guest"
RMQ_PASSWORD = "guest"


connection_params = pika.ConnectionParameters(
    host=RMQ_HOST,
    port=RMQ_PORT,
    credentials=pika.PlainCredentials(RMQ_USER, RMQ_PASSWORD),
)


async def get_connection() -> pika.BlockingConnection:
    return await aio_pika.connect_robust(connection_params)
