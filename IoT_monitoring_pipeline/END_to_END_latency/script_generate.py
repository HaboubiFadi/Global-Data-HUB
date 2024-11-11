# schedule jobs
import  threading
import time
from datetime import datetime,timedelta
import string
import random
import paho.mqtt.client as mqtt 
time.sleep(10)
# Data type inserted that we look for generate 
var_types=[['Adresse','s',30],['Mileage','int',8],['Fuel_level','reel',100],['Timestamp','time',0],['Speed','reel',300],['Longitude','reel',180]]

# Function related to MQTT broker : 
def on_connect(client, userdata, flags, return_code):
    if return_code == 0:
        print("connected")
    else:
        print("could not connect, return code:", return_code)


broker_hostname = "localhost"
port = 1883 
user='user2'
password='user2'
client = mqtt.Client("Client1")
client.username_pw_set(username=user, password=password) 
client.on_connect = on_connect

client.connect(broker_hostname, port)
client.loop_start()

topic = "Test1"




import json

def job():
    dic=generate_document(var_types,1)
    try :
        result = client.publish(topic,str(dic))
        
        status = result[0]
        if status == 0:
            print("msg is published to topic " + topic)
        else:
            print("Failed to send message to topic " + topic)
            if not client.is_connected():
                print("Client not connected, exiting...")
                    
    except Exception as e:
        print(e)
        client.disconnect()

        client.loop_stop()

    print('time now',datetime.now())








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
        print(liste_dict)  
        return liste_dict


def run_threaded(job_func):
   job_thread = threading.Thread(target=job_func)
   job_thread.start()

while True:
   run_threaded(job)
   time.sleep(0.99)