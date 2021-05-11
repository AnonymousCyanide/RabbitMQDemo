try :
    import pika
    from sensor import Sensor
except Exception as e :
    print("Some module is missing {}".format_map(e))
class RabbitMQ(object):
    def __init__(self, routing_key, exchange ='mydirex'):
        self._exchange = exchange
        self._routing_key = routing_key
        # Makes connection to given link
        self._connection = pika.BlockingConnection(
          pika.ConnectionParameters(host='localhost'))
        # Creates channel out of the connection
        self._channel = self._connection.channel()
        # Makes an exchange and specifies it's type 
        self._channel.exchange_declare(exchange = exchange , exchange_type = 'direct')
    def publish(self , payload={}):
        # sends the payload to exchange
        self._channel.basic_publish(exchange= self._exchange,
        routing_key = self._routing_key,
        body = str(payload)
        
        )

        print('Message published')
        # closing connections
        self._connection.close()

if __name__ == '__main__':
    print('Send message to ?')
    routing_key = input()
    server = RabbitMQ(routing_key = str(routing_key) ,exchange='mydirex')
    server.publish(payload=Sensor.get_values())








