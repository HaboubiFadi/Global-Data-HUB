
from pymongo import MongoClient

class mongo_instance():
    def __init__(self):
        user='admin'
        password='admin'
        host='localhost'
        port='27017'
        self.client = MongoClient("mongodb://admin:admin@localhost:27017")
        #self.client = MongoClient("mongodb://localhost:27017")
        
        self.db = self.client['Data']
        try: 
            self.db.command("serverStatus")
            print('Success')
        except Exception as e: 
            print('Error',e)
    def create_database(self,db_name):
        print(self.client[db_name])
    def create_collection(self,collection_name,db_name):
        db=self.client[db_name]
        collection=db[collection_name]
        print(db.list_collection_names())
    
    def insert_document(self,db_name,collection_name,doc):
        db=self.client[db_name]
        collection=db[collection_name]
        if isinstance(doc,list):
            print(collection.insert_many(doc))


        elif isinstance(doc,dict):     
            print(collection.insert_one(doc))

    def fetch_data(self,db_name,collection_name,query):
        db=self.client[db_name]
        collection=db[collection_name]
        result=collection.find(query)
        for i in result:
            print(i)
    def delete_data(self,db_name,collection_name,query):
        db=self.client[db_name]
        collection=db[collection_name]
        print(collection.delete_many(query))

    def drop_collection(self,db_name,collection_name):
        db=self.client[db_name]
        collection=db[collection_name]
        print(collection.drop())
        
        
if __name__=='__main__':
    mg_instance=mongo_instance()
    #mg_instance.create_database('Test')
    #mg_instance.create_collection('test1','Test')
    doc={'name':'fadi'}
    mg_instance.insert_document('Test','test1',doc)
