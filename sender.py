try :
    import pika
    from sensor import Sensor
except Exception as e :
    print("Some module is missing {}".format_map(e))
class RabbitMQ(object):
    def __init__(self, q ='hello'):
        self._connection = pika.BlockingConnection(
          pika.ConnectionParameters(host='localhost'))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=q)
    def publish(self , payload={}):
        self._channel.basic_publish(exchange='',
        routing_key ='testq',
        body = str(payload))
        print('Message published')
        self._connection.close()

if __name__ == '__main__':
    server = RabbitMQ(q='testq')
    server.publish(payload=Sensor.get_values())








