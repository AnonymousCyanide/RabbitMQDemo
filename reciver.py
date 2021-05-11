try :
    import pika
    from mongo_connect import Database
    import ast
except Exception as e :
    print("Some module is missing {}".format_map(e))

class RabbitMQ(object):
    def __init__(self,callbackf,q='testq'):
       # Makes connection to given link
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        # Creates channel out of the connection
        self._channel = self._connection.channel()
        # Looks for queue to get info from 
        # durable = True means data won't be lost 
        self._channel.queue_declare(queue=q, durable = True)
        # Specifies which q to consume from and calls the function mentioned 
        self._channel.basic_consume(queue=q, on_message_callback = callbackf)
   
    def consume(self):
        print("[O] Waiting for message")
        # makes sure one task is completed before taking another
        self._channel.basic_qos(prefetch_count = 1)
        # Starts accepting tasks
        self._channel.start_consuming()




def callback(ch, method, properties, body ):
    
    db = Database()
    obj = ast.literal_eval(body.decode('utf-8'))
    time= obj['time']
    data = obj['data']
    db.add_data(time=time ,data=data)

    try :
        db = Database()
        obj = ast.literal_eval(body.decode('utf-8'))
        time= obj['time']
        data = obj['data']
        db.add_data(time=time ,data=data)
        ch.basic_ack(delivery_tag = method.delivery_tag)
        print(method.delivery_tag)
        print("[o] recived and uploaded  %r"%body)
    except Exception as e:
        print('Some problem has occured ')
        print(e)
    
    
if __name__ == '__main__':
    rb = RabbitMQ(q='testq',callbackf=callback)
    rb.consume()