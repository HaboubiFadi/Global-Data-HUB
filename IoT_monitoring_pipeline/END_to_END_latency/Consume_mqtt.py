import paho.mqtt.client as mqtt
import time
from kafka_class import Singleton_kafka_producer
dic={'bootstrap.servers': 'localhost:9092'}

topic='Test1'
def on_connect(client, userdata, flags, return_code):
    if return_code == 0:
        print("connected")
        client.subscribe(topic)
    else:
        print("could not connect, return code:", return_code)
        client.failed_connect = True


topic_kafka='test_kafka'

kafka_class=Singleton_kafka_producer()
kafka_class.initiate(configuration_server=dic,topic=topic_kafka)
def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))
    kafka_class.produce('key',message.payload.decode("utf-8"))


broker_hostname ="localhost"
port = 1883 

client = mqtt.Client("Client2")
client.username_pw_set(username="user2", password="user2") # uncomment if you use password auth
client.on_connect = on_connect
client.on_message = on_message
client.failed_connect = False
client.connect(broker_hostname,port)

client.loop_start()

topic_kafka = 'init_test_kafka'
dic={'bootstrap.servers': 'broker:9092'}

try:
    i = 0
    while i < 100 and client.failed_connect == False:
        time.sleep(1)

        i = i + 1

    if client.failed_connect == True:
        print('Connection failed, exiting...')

finally:
    client.disconnect()
    client.loop_stop()