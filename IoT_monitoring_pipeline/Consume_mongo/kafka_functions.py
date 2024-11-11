from confluent_kafka import Producer,Consumer
import time
import json
import logging
import sys
from datetime import datetime


logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')



def initiat_producer(configuration_server):
    producer_init = Producer(configuration_server)
    
    return producer_init


def assignment_callback(consumer,topic_partitions):
    for tp in topic_partitions:
        print(tp.topic)
        print(tp.partition)
        print(tp.offset)    


def Initiat_Consumers(configuration_server,topic_liste):
    consumer_init = Consumer(configuration_server)
    consumer_init.subscribe(topic_liste,on_assign=assignment_callback)
    
    return consumer_init



def Consume_data(consumer):
    
    while True:
    
        msg=consumer.poll(1.0)

        if msg is None:
            print('no data yet')
            continue
        if msg.error():
            print(f"There might be a problem {msg.error()}")
            continue
            

        #print(msg.value())





def Consume_data_mongo(mongo_instance,db_name,collection_name,consumer):
    
    while True:
    
        msg=consumer.poll(1.0)

        if msg is None:
            #print('no data yet')
            continue
        if msg.error():
            print(f"There might be a problem {msg.error()}")
            continue

    
        dic={'id':msg.key().decode('utf-8'),'timestamp':datetime.timestamp(datetime.now()),'type':'kafka_metric_consume'}
        logging.info(f'{json.dumps(dic)}')
        # Parse the JSON string into a JSON object
        json_object = json.loads(msg.value().decode('utf-8'))

           
        db_name='Test'
        collection_name='test1'
        mongo_instance.insert_document(db_name,collection_name,json_object)

        dic={'id':msg.key().decode('utf-8'),'timestamp':datetime.timestamp(datetime.now()),'type':'mongo_metric_sink'}
        logging.info(f'{json.dumps(dic)}')



