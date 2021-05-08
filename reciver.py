try :
    import pika
except Exception as e :
    print("Some module is missing {}".format_map(e))
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='Hi')
def callback(ch, method, properties, body ):
    print("recived "%body)
channel.basic_consume(
    queue='hi',
    on_message_callback = callback,
    auto_ack=True
)   
print("Waiting for message")
channel.start_consuming()