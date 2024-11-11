import paho.mqtt.client as mqtt 
import time 


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
msg_count = 0

try:
    while msg_count < 10:
        time.sleep(1)
        msg_count += 1
        result = client.publish(topic, msg_count)
        status = result[0]
        if status == 0:
            print("Message "+ str(msg_count) + " is published to topic " + topic)
        else:
            print("Failed to send message to topic " + topic)
            if not client.is_connected():
                print("Client not connected, exiting...")
                break
finally:
    client.disconnect()
    client.loop_stop()