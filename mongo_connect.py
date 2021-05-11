try:
    import pymongo
    from pymongo import MongoClient
except Exception as e:
    print('Some modules are missing')
# Gets cluster key from loacal text file
key = open('connect_key.txt','r').read()

class Database(object):
    def __init__(self,cluster_key=key,db_name='RabbitMQData',collection_name='data'):
       
        self._cluster_key= cluster_key
        self.db_name =db_name
        self.collection_name = collection_name
        # Connects to mongo client and gets cluster using cluster key
        self.cluster = MongoClient(self._cluster_key)
        # Points to the database from the cluster
        self.db = self.cluster[self.db_name]
        # Points to the collection in the database 
        self.collection = self.db[self.collection_name]
           
     # used to add data to database        
    def add_data(self,time,data):
        # making a post to put into Db
        # Id is the db count hence starts from 0 and is incresed by 1 with every new item
        # Takes time and data as argument
        post ={
            '_id':self.collection.count_documents({}),
            'time':time,
            'data':data
        }
        # Performs insert operation on the db 
        self.collection.insert_one(post)

if __name__ =='__main__':
    db = Database()
    db.add_data(time='3pm',data='124')

