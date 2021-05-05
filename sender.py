try :
    import pika
except Exception as e :
    print("Some module is missing {}".format_map(e))