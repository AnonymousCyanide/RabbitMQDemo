try :
    import pika
    from mongo_connect import Database
    import ast
except Exception as e :
    print("Some module is missing {}".format_map(e))


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='testq')
def callback(ch, method, properties, body ):
    db = Database()
    
    obj = ast.literal_eval(body.decode('utf-8'))
    time= obj['time']
    data = obj['data']
    db.add_data(time=time ,data=data)
    print("[o] recived and uploaded  %r"%body)
    
channel.basic_consume(
    queue='testq',
    on_message_callback = callback,
    auto_ack=True
)   
print("Waiting for message")
channel.start_consuming()