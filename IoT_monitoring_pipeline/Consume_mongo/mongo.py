
from pymongo import MongoClient

class mongo_instance():
    def __init__(self):
        self.client = MongoClient("mongodb://admin:admin@mongodb:27017")

        #self.client = MongoClient("http://mongodb:27017")
        self.db = self.client['Data']
        try: 
            self.db.command("serverStatus")
        except Exception as e: 
            print('Error',e)
    def create_database(self,db_name):
        student_db=self.client[db_name]
    def create_collection(self,collection_name,db_name):
        db=self.client[db_name]
        collection=db[collection_name]
        db.list_collection_names()
    
    def insert_document(self,db_name,collection_name,doc):
        db=self.client[db_name]
        collection=db[collection_name]
        if isinstance(doc,list):
            collection.insert_many(doc)


        elif isinstance(doc,dict):     
            collection.insert_one(doc)

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
        
        


   
