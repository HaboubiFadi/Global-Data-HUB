import docker
import json

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from datetime import datetime
from sqlalchemy import Column,Table,Integer,String,DateTime,TIMESTAMP,BigInteger
# This is where we declare our database 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine,text
from psycopg2.extensions import register_adapter, AsIs
import numpy as np
register_adapter(np.int64, AsIs)
# Create an Engine
engine_string='postgresql://admin:admin@localhost:5432/postgres'
engine = create_engine(engine_string, echo=True)



Session = sessionmaker(bind=engine) # Session for database manipulation

Base = declarative_base() # this variable is for mapping entites into database

class mqtt_metric_consume(Base):
    __tablename__='mqtt_metric_consume'
    id_object=Column(Integer,primary_key=True)
    id =Column(BigInteger)
    
    timedate=Column(DateTime)
   
    
    def __init__(self,dic):
        self.id=dic['id']

        date=dic['time']


        self.timedate=date
    def fill_object(self,dic):
        self.id=dic['id']

        date=dic['time']


        self.timedate=date    
class mqtt_metric_produce(Base):
    __tablename__='mqtt_metric_produce'
    id_object=Column(Integer,primary_key=True)
    id =Column(BigInteger)
    
    timedate=Column(DateTime)
   
    
    def __init__(self,dic):
        self.id=dic['id']

        date=dic['time']


        self.timedate=date
class kafka_metric_consume(Base):
    __tablename__='kafka_metric_consume'
    id_object=Column(Integer,primary_key=True)
    id =Column(BigInteger)
    
    timedate=Column(DateTime)
   
    
    def __init__(self,dic):
        self.id=dic['id']

        date=dic['time']


        self.timedate=date
    def fill_object(self,dic):
        self.id=dic['id']

        date=dic['time']


        self.timedate=date    
class kafka_metric_produce(Base):
    __tablename__='kafka_metric_produce'
    id_object=Column(Integer,primary_key=True)
    id =Column(BigInteger)
    
    timedate=Column(DateTime)
   
    
    def __init__(self,dic):
        self.id=dic['id']

        date=dic['time']


        self.timedate=date
    def fill_object(self,dic):
        self.id=dic['id']

        date=dic['time']


        self.timedate=date    
class mongo_metric_sink(Base):
    __tablename__='mongo_metric_sink'
    id_object=Column(Integer,primary_key=True)
    id =Column(BigInteger)
    
    timedate=Column(DateTime)
   
    
    def __init__(self,dic):
        self.id=dic['id']

        date=dic['time']


        self.timedate=date   
    def fill_object(self,dic):
        self.id=dic['id']

        date=dic['time']


        self.timedate=date
Base.metadata.drop_all(engine)                                         
Base.metadata.create_all(engine)





































import random
import sys
import asyncio

from sqlalchemy import create_engine,text

# Create an Engine
engine_string='postgresql://admin:admin@localhost:5432/postgres'
import pytz
engine = create_engine(engine_string, echo=True)
# Execute a Custom SQL Query
#sql_query = text("INSERT INTO mqtt_metric_produce (id, timestamp) VALUES (:id, :timestamp)")
from sqlalchemy.sql import text

def choose_object(log,log_type):
    if log_type=='kafka_metric_consume':
        return kafka_metric_consume(log)
    elif log_type=='kafka_metric_produce':
        return kafka_metric_produce(log)
    elif log_type=='mqtt_metric_produce':
        return mqtt_metric_produce(log)
    elif log_type =='mqtt_metric_consume':
        return mqtt_metric_consume(log)
    elif log_type =='mongo_metric_sink':
        return mongo_metric_sink(log)

def sink_log(logs):
    session=Session()
    
    for log in logs:
        
        log['time']=datetime.fromtimestamp(log['timestamp'])
        object_log=choose_object(log,log['type'])
        session.add(object_log)  
    
    session.commit()
    session.close()







client = docker.from_env()
print(client.containers.list())
list_containers_name=['generate_image','consume_mqtt','consume_kafka_mongo']

def match_string_liste(string,liste):
    for item in liste:
        if item in string:
            return True
    return False    
def Get_required_containers(list_containers_name):
    active_containers_liste=client.containers.list()
    containers_list_required=[]
    print(client.containers.list())
    for container in active_containers_liste:
        if match_string_liste(container.name ,list_containers_name):
            print(container.name)
            containers_list_required.append(container)
    return  containers_list_required     
containers=Get_required_containers(list_containers_name)

from datetime import timedelta
async def Logs(container,timer):
    objects=[]
    i=0
    print('this the container name',container.name)
    start_time=datetime.now()
    for line in container.logs(stream=True):
      
        try:
            json_object = json.loads(line.strip().decode('utf-8'))
            print('type',json_object['type'])
            objects.append(json_object)
                
        except:
            print('Error')
            continue  
        
        
        print('this the container name',container.name)

        print(line.strip())
        i+=1
        print(i)

        if i>timer:
            sink_log(objects)
            objects=[]
            await asyncio.sleep(2)

# Query  Avg latency SELECT AVG(extract(epoch from (mqtt.timestamp -mongo.timestamp))) as avg_time_difference
#          FROM mqtt_metric_producer mqtt
            # JOIN mongo_metric_sink mongo ON mqtt.id =mongo.id 
# percentile
            # SELECT percentile_cont(0.25) WITHIN GROUP(ORDER BY mongo.timestamp -mqtt.timestamp) AS percentile_10,4
            #          FROM mqtt_metric_producer mqtt
            # JOIN mongo_metric_sink mongo ON mqtt.id =mongo.id    



async def main():
    tasks = [asyncio.create_task(Logs(containe,3)) for containe in containers]

    await asyncio.sleep(100000)

    for task in tasks:
        task.cancel()

    await asyncio.wait(tasks)



if __name__ == "__main__":
    asyncio.run(main())