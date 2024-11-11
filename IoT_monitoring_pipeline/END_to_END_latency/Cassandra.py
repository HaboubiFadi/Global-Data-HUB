
from cassandra.cluster import Cluster
from IoT_instance import IoT_instance
from cassandra.cqlengine import connection
from cassandra.cluster import Cluster
from cassandra.cqlengine.management import sync_table
import pandas as pd



class Cassandra_instance():
    
    def __init__(self,server,keyspace):
            print('s1')
 
            self.cluster=Cluster(server,port=9042)
            print('s1')
            self.session= self.cluster.connect()
            print('s3')
            self.keyspace=keyspace
            self.server=server
            print(self.server)
            connection.setup(server, keyspace)

            connection.register_connection(keyspace, session=self.session)

            
           
        

    

    def create_keyspace(self,keyspace,replication_factor=1):
        query="CREATE KEYSPACE IF NOT EXISTS "+keyspace +"WITH REPLICATION = {'class':'SimpleStrategy','replication_factor':1 }"
        try:
            self.session.execute(query)
        except Exception as e :
            print(e)  


    def create_table(self,model_class):
        try:
            sync_table(model_class)
        except Exception as e:
            print(e)
    def insert_data(self,model_class,dic):
        connection.setup(self.server, self.keyspace)

            # Register the model    
        connection.register_connection(self.keyspace, session=self.session)
        print(model_class.create(**dic))




        

    

    def delete_doc_with_id(self,model_class,data_id):
        record=model_class.get(id=data_id)
        record.delete()

        

    def search_data_with_id(self,model_class):
        all_objects=model_class.objects().all()
        for obj in all_objects:
            print(obj.Adresse)


if __name__=='__main__':
    keyspace='test'
    server=['127.0.0.1']

    cas_ins=Cassandra_instance(server,keyspace)
    dic={'Adresse':'fadi'}
    cas_ins.create_table(IoT_instance)
    #cas_ins.insert_data(IoT_instance,dic)
    #cas_ins.search_data_with_id(IoT_instance)