try:
    import pymongo
    from pymongo import MongoClient
except Exception as e:
    print('Some modules are missing')
key = 'mongodb+srv://Avi:avi1234@cluster0.2weff.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
class Database(object):
    def __init__(self,cluster_key=key,db_name='RabbitMQData',collection_name='data'):
            self.cluster_key= cluster_key
            self.db_name =db_name
            self.collection_name = collection_name
            self.cluster = MongoClient(cluster_key)
            self.db = cluster[self.db_name]
            self.collection = db[self.collection_name]
    def add_data(time,data):
        post ={
            '_id':self.collection.count_documents({}),
            'time':time,
            'data':data
        }
        self.collection.insert_one(post)





