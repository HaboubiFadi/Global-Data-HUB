# schedule jobs
import  threading
import time
from datetime import datetime,timedelta
import string
import random
import paho.mqtt.client as mqtt 
import os
import json

import logging
import sys
from datetime import datetime

# sleeping time waiting for the initiating of the servers .
time.sleep(10)
# Data type inserted that we look for generate 

var_types=[['Adresse','s',30],['Mileage','int',8],['Fuel_level','reel',100],['Speed','reel',300],['Longitude','reel',180]]


interval_time=os.environ.get('interval_time') # interval between time generation.





# Function related to MQTT bromqttker : 
def on_connect(client, userdata, flags, return_code):
    if return_code == 0:
        print("connected")
    else:
        print("could not connect, return code:", return_code)

# Enviorement variables declaration 
broker_hostname = os.environ.get('broker_hostname')
port = int(os.environ.get('port')) 
user=os.environ.get('user')
password=os.environ.get('password')
monitoring_port=os.environ.get('monitoring_port')
client_name=os.environ.get('client_name')
topic = os.environ.get('topic')


# mqtt client initiation
client = client = mqtt.Client(client_name)
client.username_pw_set(username=user, password=password) 
client.on_connect = on_connect
client.connect(broker_hostname, port)
client.loop_start()



def job():
    dic=generate_document(var_types,1)
   
    generate_id=generate_type('int',10)
    dic['id']=generate_id
    try :
        json_data = json.dumps(dic)
        result = client.publish(topic,json_data)
        
        # increament the mqtt_monitor_metric timestamp after a publish into the mqtt topic
        logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')

        # Example log message
        dic={'id':dic['id'],'timestamp':datetime.timestamp(datetime.now()),'type':'mqtt_metric_produce'}
        logging.info(f'{json.dumps(dic)}')





        status = result[0]
        if status == 0:
            #print("msg is published to topic " + topic)
            pass
        else:
            #print("Failed to send message to topic " + topic)
            if not client.is_connected():
                print("Client not connected, exiting...")
                    
    except Exception as e:
        client.disconnect()

        client.loop_stop()









def generate_type(c_type,length):
    if c_type=='s':
        res=''.join(random.choices(string.ascii_letters,k=length))

        return str(res)
    elif c_type=='int':
        rand_int=random.randint(0,10**length)
        return rand_int
    elif c_type=='time':
        td = datetime(2024,1,1)+(random.uniform(0,100))* timedelta(days=1)
        return str(td)
    elif c_type=='reel':
        real=random.uniform(0,length)
        return real
def generate_document(var_types,multiple=1):
    if multiple<=1:
        dic={}

        for lis in var_types:
            dic[lis[0]]=generate_type(lis[1],lis[2])
        return dic    
    else:
        liste_dict=[{} for i in range(multiple)]
        for lis in var_types:
            for i in range(len(liste_dict)):
                generated=generate_type(lis[1],lis[2])
                liste_dict[i][lis[0]]=generated
        return liste_dict



def run_threaded(job_func):
   job_thread = threading.Thread(target=job_func)
   job_thread.start()

if __name__ == "__main__":
    while True: 
        # period between collection
        run_threaded(job)
        time.sleep(int(interval_time))