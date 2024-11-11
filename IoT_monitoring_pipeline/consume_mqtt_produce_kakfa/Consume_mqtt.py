import paho.mqtt.client as mqtt
import time
from kafka_class import Singleton_kafka_producer
import os
from prometheus_client.core import Gauge, Counter
from prometheus_client import start_http_server
import json
import logging
import sys

from datetime import datetime



time.sleep(10)
# monitoring variables
#mqtt_metric_consume=Gauge('mqtt_metric_consume','time for the Consuming  data from mqtt topic ',['id'])
#kafka_metric_produce=Gauge('kafka_metric_produce','time for the publish of data into kafka topic ',['id'])

            ## Begin Variables Declaration ##
kafka_broker=os.environ.get('kafka_broker')
dic={'bootstrap.servers':str(kafka_broker) }
topic_kafka=os.environ.get("topic_kafka")


topic=os.environ.get('topic_mqtt')
monitoring_port=os.environ.get('monitoring_port')
broker_hostname =os.environ.get("broker_hostname")

port = 1883 
kafka_class=Singleton_kafka_producer()

kafka_class.initiate(configuration_server=dic,topic=topic_kafka)
user=os.environ.get('user')
password=os.environ.get('password')
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s') # logging Format Initiatiing 


            ## END  Variables Declaration ##

        ## Configure callbacks and connect a client to your broker ##
def on_connect(client, userdata, flags, return_code):
    if return_code == 0:
        print("connected")
        client.subscribe(topic)
    else:
        print("could not connect, return code:", return_code)
        client.failed_connect = True




def on_message(client, userdata, message):
    # Convert string to json(dic) to get monitoring_id 
    json_object = json.loads(str(message.payload.decode("utf-8")))
    monitoring_id=json_object['id']
    

    dic={'id':json_object['id'],'timestamp':datetime.timestamp(datetime.now()),'type':'mqtt_metric_consume'}
    logging.info(f'{json.dumps(dic)}')

    kafka_class.produce(monitoring_id,message.payload.decode("utf-8"))
    dic={'id':json_object['id'],'timestamp':datetime.timestamp(datetime.now()),'type':'kafka_metric_produce'}
    logging.info(f'{json.dumps(dic)}')



client = mqtt.Client("Client2")
client.username_pw_set(username=user, password=password)
client.on_connect = on_connect
client.on_message = on_message
client.failed_connect = False
client.connect(broker_hostname,port)


            ## End Configure ##

#start_http_server(int(monitoring_port))


## Start Consuming From mqtt 
client.loop_start()


try:
    while True and client.failed_connect == False:
        time.sleep(1)


    if client.failed_connect == True:
        print('Connection failed, exiting...')

finally:
    client.disconnect()
    client.loop_stop()