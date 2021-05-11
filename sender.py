try :
    import pika
    from sensor import Sensor
except Exception as e :
    print("Some module is missing {}".format_map(e))
class RabbitMQ(object):
    def __init__(self, q ='testq'):
        # Makes connection to given link
        self._connection = pika.BlockingConnection(
          pika.ConnectionParameters(host='localhost'))
        # Creates channel out of the connection
        self._channel = self._connection.channel()
        # Looks for queue to put in message 
        # durable = True means data won't be lost
        self._channel.queue_declare(queue=q , durable = True)
    def publish(self , payload={}):
        # sends the payload to queue
        self._channel.basic_publish(exchange='',
        routing_key ='testq',
        body = str(payload),
        delivery_mode = 2
        )

        print('Message published')
        # closing connections
        self._connection.close()

if __name__ == '__main__':
    server = RabbitMQ(q='testq')
    server.publish(payload=Sensor.get_values())








