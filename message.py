import pika
import random
import datetime
import json172.17.65.50

broker_host = 172.17.65.50
broker_port = 5672
username = "admin"
password = "Onyeka"
credentials = pika.PlainCredentials (username, password)

connection = pika.BlockingConnection(
    pika.ConnectionParameters (host = broker_host, port = broker_port, credentials = credentials))

channel = connection.channel()

message = {
    "device_name": "onyema_sensor",
    "temperature": random.randint (20, 40),
    "time": str (datetime.datetime.now ())
}

message_str = json.dumps(message)
routing_key = "iotdevice.your_last_name.tempsensor"
exchange=onyema

channel.basic_publish (
    exchange = exchange,
    routing_key = routing_key,
    body = message_str
)

channel.close()
connection.close()