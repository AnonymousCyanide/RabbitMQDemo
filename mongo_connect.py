try:
    import pymongo
    from pymongo import MongoClient
except Exception as e:
    print('Some modules are missing')
key = open('connect_key.txt','r').read()

class Database(object):
    def __init__(self,cluster_key=key,db_name='RabbitMQData',collection_name='data'):
           
        self._cluster_key= cluster_key
        self.db_name =db_name
        self.collection_name = collection_name
        self.cluster = MongoClient(self._cluster_key)
        self.db = self.cluster[self.db_name]
        self.collection = self.db[self.collection_name]
           
            
    def add_data(self,time,data):
        post ={
            '_id':self.collection.count_documents({}),
            'time':time,
            'data':data
        }
        self.collection.insert_one(post)

if __name__ =='__main__':
    db = Database()
    db.add_data(time='3pm',data='124')

