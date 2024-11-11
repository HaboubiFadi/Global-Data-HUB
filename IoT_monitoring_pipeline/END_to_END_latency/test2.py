from sqlalchemy import create_engine,text
from psycopg2.extensions import register_adapter, AsIs
import numpy as np
register_adapter(np.int64, AsIs)
# Create an Engine
engine_string='postgresql://admin:admin@localhost:5432/postgres'
import pytz
engine = create_engine(engine_string, echo=True)
# Execute a Custom SQL Query
#sql_query = text("INSERT INTO mqtt_metric_produce (id, timestamp) VALUES (:id, :timestamp)")
import pandas as pd
 
# Create a Timestamp object
timestamp = pd.Timestamp("2022-10-12 12:30:45")
 
# Convert to Unix time
unix_time = timestamp.timestamp()
print(timestamp)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from datetime import datetime
from sqlalchemy import Column,Table,Integer,String,DateTime,TIMESTAMP
# This is where we declare our database 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Session = sessionmaker(bind=engine) # Session for database manipulation

Base = declarative_base() # this variable is for mapping entites into database

class mqtt_metric_consume(Base):
    __tablename__='mqtt_metric_consume'
    id_ticket=Column(Integer,primary_key=True)
    id =Column(Integer)
    
    last_time_updated=Column(DateTime)
   
    
    def __init__(self,dic):
        self.id=dic['id']

        date=dic['time']


        self.last_time_updated=date
    def fill_object(self,dic):
        self.id=dic['id']

        date=dic['time']


        self.last_time_updated=date    
class mqtt_metric_produce(Base):
    __tablename__='mqtt_metric_produce'
    id_ticket=Column(Integer,primary_key=True)
    id =Column(Integer)
    
    last_time_updated=Column(DateTime)
   
    
    def __init__(self,dic):
        self.id=dic['id']

        date=dic['time']


        self.last_time_updated=date
class kafka_metric_consume(Base):
    __tablename__='kafka_metric_consume'
    id_ticket=Column(Integer,primary_key=True)
    id =Column(Integer)
    
    last_time_updated=Column(DateTime)
   
    
    def __init__(self,dic):
        self.id=dic['id']

        date=dic['time']


        self.last_time_updated=date
    def fill_object(self,dic):
        self.id=dic['id']

        date=dic['time']


        self.last_time_updated=date    
class kafka_metric_produce(Base):
    __tablename__='kafka_metric_produce'
    id_ticket=Column(Integer,primary_key=True)
    id =Column(Integer)
    
    last_time_updated=Column(DateTime)
   
    
    def __init__(self,dic):
        self.id=dic['id']

        date=dic['time']


        self.last_time_updated=date
    def fill_object(self,dic):
        self.id=dic['id']

        date=dic['time']


        self.last_time_updated=date    
class mongo_metric_sink(Base):
    __tablename__='mongo_metric_sink'
    id_ticket=Column(Integer,primary_key=True)
    id =Column(Integer)
    
    last_time_updated=Column(DateTime)
   
    
    def __init__(self,dic):
        self.id=dic['id']

        date=dic['time']


        self.last_time_updated=date   
    def fill_object(self,dic):
        self.id=dic['id']

        date=dic['time']


        self.last_time_updated=date                                 
Base.metadata.create_all(engine)




import pandas as pd
 
# Create a Timestamp object
timestamp = pd.Timestamp("2022-10-12 12:30:45")
 
# Convert to Unix time
unix_time = timestamp.timestamp()



Data=mqtt_metric_consume({'id':1,'time':datetime.now()})



Session = sessionmaker(bind=engine) # Session for database manipulation
session=Session()
if isinstance(Data,list):
    session.add_all(Data)
else:
    session.add(Data)  
    session.commit()
    session.close()



import time
def sink_log(logs,Class):
    session=Session()
    
    for log in logs:
        log['time']=datetime.fromtimestamp(log['timestamp'])
        Class.fill_object(log)
        session.add(Class)  
    
    session.commit()
    session.close()



















with engine.connect() as con:

    line = {"id": '1' ,'timestamp':timestamp}
             
    
    test="mqtt_metric_produce"
    statement = text(f"INSERT INTO {test}(id,datetime) VALUES(:id,:timestamp)")

    
    con.execute(statement, line)
    con.commit()


























"""
client = docker.from_env()
print(client.containers.list())
container = client.containers.get('pfe_generate_image_1')
print(container.name)

i=0"""


"""for line in container.logs(stream=True):
    print(line.strip())
    i+=1
    print(i)
    try:
        json_object = json.loads(line.strip().decode('utf-8'))
        print(json_object['id'])
    except:
        print('Error')    """


"""specific_info=[container,i]

timer=0"""

'''def extract_logs(specific_info,max_time):
    timer=0
    objects=[]
    j=0
    container=specific_info[0]
    for line in container.logs(stream=True):

        if timer>max_time:
                break
        elif j>=specific_info[1] :
              timer+=1
              try:
                print('im here')
                json_object = json.loads(line.strip().decode('utf-8'))
                objects.append(json_object)
                
              except:
                print('Error')  
        
        print(j)
        j+=1
    print('len of object ',len(objects))           
    print(j)    
    return [container,j]
import time     
for i in range(5):
        print(specific_info[1])
        specific_info=extract_logs(specific_info,100)  
        print('stop')
        time.sleep(5)  
'''
"""import asyncio


import asyncio
import random
import time

import asyncio


async def prints_quickly():
    i=0
    while True:  # runs forever
        await asyncio.sleep(1)

        i+=1
        print("quick!")
        print(i)


async def prints_slowly():
    i=0
    while True:  # runs forever
        await asyncio.sleep(1)  
        i+=1
        print("slow!")
        print(i)


async def print_test():
    i=0
    while True:  # runs forever
        await asyncio.sleep(1)  
        i+=1
        print("test!")
        print(i)



async def main():
    tasks = [asyncio.create_task(prints_quickly(), name="quick"), 
             asyncio.create_task(prints_slowly(), name="slow"),
             asyncio.create_task(print_test(),name="test")]

    await asyncio.sleep(100000)

    for task in tasks:
        task.cancel()

    await asyncio.wait(tasks)

    print("Out!")


if __name__ == "__main__":
    asyncio.run(main())"""