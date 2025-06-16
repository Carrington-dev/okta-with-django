import json
import random
import time
import uuid
import pika
import requests

class RabbitMQ:
    def __new__(cls, username, password, host, port):
        if not hasattr(cls, 'instance'):
            cls.instance = super(RabbitMQ, cls).__new__(cls)
        return cls.instance

    def __init__(self, username, password, host, port):
        self.credentials = pika.PlainCredentials(username=username, password=password)
        self.parameters = pika.ConnectionParameters(host=host, port=port, credentials=self.credentials)
        self.connection = pika.BlockingConnection(self.parameters)
        self.queue = 'letterhead'
        self.channel = self.connection.channel()
    
    def declare_queue(self, queue):
        self.channel.queue_declare(queue=queue)
    
    def recieve_message(self, ):
        if not self.connection or self.connection.is_closed:
            print("I am disconnected")
            return
        self.declare_queue(self.queue)
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=self.queue,  on_message_callback=self.do_what_on_message)
        print("Consuming")
        self.channel.start_consuming()

    def send_message(self, exchange,  routing_key, data):
        if not self.connection or self.connection.is_closed:
            print("I am disconnected")
            return
        self.declare_queue(self.queue)
        self.channel.basic_publish(exchange=exchange,  routing_key=routing_key, body= data)
        print(data)
        self.connection.close()
                

    def do_what_on_message(self, channel, method, properties, body):
        print(f"Recieved Data { body }")
        # bo = json.loads(body)
        response = requests.post(
            url='http://localhost:8000/api/v1/auth/users/', 
            json=json.loads(body),
            headers={"Content-Type":"application/json"}
        )
        print(response.text)
        channel.basic_ack(delivery_tag=method.delivery_tag)





# sender = RabbitMQ('guest', 'guest', 'localhost', 5672)
