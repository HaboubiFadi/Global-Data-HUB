from confluent_kafka import Producer,Consumer

from nifi_api_function import Trigger_flow
import pandas as pd


def Serialization(DataFrame):
    return DataFrame.to_json()

def initiat_producer(configuration_server):
    producer_init = Producer(configuration_server)
    
    return producer_init



def Deserialization(s):

    json_string = s.decode('utf-8')
    df = pd.read_json(json_string)
    
        
    return df
def produce_data(producer,data,key,topic):
    
    
    print('/n data_key:',key)

    
    
    
    serliazed=Serialization(data)
    resultat=producer.produce(topic, key=key, value=serliazed)
    print(resultat)
    producer.flush()


def assignment_callback(consumer,topic_partitions):
    for tp in topic_partitions:
        print(tp.topic)
        print(tp.partition)
        print(tp.offset)    


def Initiat_Consumers(configuration_server,topic_liste):
    consumer_init = Consumer(configuration_server)
    consumer_init.subscribe(topic_liste,on_assign=assignment_callback)
    
    return consumer_init



def Consume_data(consumer,nifi_host):
    
    while True:
    
        msg=consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print(f"There might be a problem {msg.error()}")
            continue
            
        Trigger_flow(nifi_host)
    
        json_string = msg.value().decode('utf-8')

        # Parse the JSON string into a JSON object
        print(json_string)








