import paho.mqtt.client as mqtt
import time
import os
from prometheus_client.core import Gauge
from prometheus_client import start_http_server


time.sleep(10)
# monitoring variables

monitoring_dic={}
broker_hostname=os.environ.get("broker_hostname")
user=os.environ.get('user')
password=os.environ.get('password')

monitoring_port=os.environ.get('monitoring_port')
start_http_server(int(monitoring_port))

topic='$SYS/#'

def on_connect(client, userdata, flags, return_code):
    if return_code == 0:
        print("connected")
        client.subscribe(topic)
    else:
        print("could not connect, return code:", return_code)
        client.failed_connect = True


def on_message(client, userdata, message):
   
    
    print(message.topic+":"+str(message.payload.decode("utf-8")))
    if str(message.topic) not in monitoring_dic:
        monitoring_dic[message.topic]=Gauge(str(message.topic)[1:].replace('/','_').replace(' ',''),str(message.topic))
    try:
        if 'seconds' in str(message.payload.decode('utf-8')):
            uptime_monitor_var=str(message.payload.decode('utf-8')).replace('seconds','').replace(' ','')
            print(uptime_monitor_var)
            monitoring_dic[message.topic].set(float(uptime_monitor_var)) 
        else:
            monitoring_dic[message.topic].set(message.payload)   
    except Exception as e:
        print("Error",e)

        print('topic of error:',message.topic)
    




port = 1883 

client = mqtt.Client("Client3")


client.username_pw_set(username=user, password=password)
client.on_connect = on_connect
client.on_message = on_message
client.failed_connect = False
client.connect(broker_hostname,port)

client.loop_start()


try:
    while True and client.failed_connect == False:
        time.sleep(1)

    if client.failed_connect == True:
        print('Connection failed, exiting...')
        

finally:
    client.disconnect()
    client.loop_stop()