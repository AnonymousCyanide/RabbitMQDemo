try :
    import pika
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
        routing_key ='Hi',
        body = str(payload))
        print('Message published')
        self._connection.close()

if __name__ == '__main__':
    server = RabbitMQ(q='Hi')
    server.publish(payload={'data':'This is the data'})








