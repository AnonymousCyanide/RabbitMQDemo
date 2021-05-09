try:
    from datetime import datetime
    import random
except Exception as e:
    print('Some modules are missing')
    
class Sensor(object):
    def __init__(self):
        pass
    def get_values():
        time = str(datetime.now())
        data = random.random()
        value ={
            'time':time,
            'data':  data
        }
        return value