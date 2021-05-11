try :
    import pika
    from sensor import Sensor
except Exception as e :
    print("Some module is missing {}".format_map(e))
class RabbitMQ(object):
    def __init__(self, exchange ='myex'):
        self._exchange = exchange
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
        routing_key ='black',
        body = str(payload)
        
        )

        print('Message published')
        # closing connections
        self._connection.close()

if __name__ == '__main__':
    server = RabbitMQ(exchange='myex')
    server.publish(payload=Sensor.get_values())








