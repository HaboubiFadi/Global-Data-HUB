from confluent_kafka import Producer,Consumer
import time
import json




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
            

        print(msg.value())

def Consume_data_cassandra(cassandra_instance,model,consumer):
    while True:
    
        msg=consumer.poll(1.0)

        if msg is None:
            print('no data yet')
            continue
        if msg.error():
            print(f"There might be a problem {msg.error()}")
            continue
            

        print(msg.value())   
        json_object = json.loads(msg.value().decode('utf-8'))
        cassandra_instance.insert_data(model,json_object)
             
