import json
from django.core.management.base import BaseCommand
from tradings.mq import RabbitMQ
from authenticate.vroomweb.settings import local


class Command(BaseCommand):
    help = 'Consumes messages from the specified queue'

    def add_arguments(self, parser):
        # pass
        parser.add_argument('letterhead', type=str, help='The name of the queue to consume messages from')

    def handle(self, *args,  **options):
        # queue_name = options['letterhead']
        # print(queue_name)
        # Define a callback function to process the received message
        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)

        publisher = RabbitMQ(**local.RABBITMQ['default'])
        publisher.send_message(
            exchange = "",  
            routing_key = 'letterhead',
            # routing_key = 'user.deleted.1.2.3',
            data = json.dumps({
                "message": 'Carrington is learning django microservices'
            })
        )

        print('Sent a message')