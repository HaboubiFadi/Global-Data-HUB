from kafka_functions import Initiat_Consumers,Consume_data
import os
from confluent_kafka.admin import AdminClient,NewTopic


import time
dic={'bootstrap.servers': 'broker:9092','group.id':'test_team'}

topic_kafka=os.environ.get("kafka_topic") # Environement variable   
print('Create Topic')

conf = {
    'bootstrap.servers': 'broker:9092'
}

topic_config = {"max.message.bytes": 15048576}

topic_list=[]
topic_list.append(NewTopic(
    topic=topic_kafka,
    num_partitions=1,
    replication_factor=1,
    # replica_assignment=replica_assignment,
    config=topic_config
)
)
admin=AdminClient(conf)

admin.create_topics(topic_list)
time.sleep(3)
print(admin.list_topics().topics)


print('\n\n ################################################# \n \n')

print('Start Consumer')
# nifi_host='http://localhost:8000/nifi-api/' # this represent nifi local adresse that can only be accessed from the host
nifi_host="http://nifi:8080/nifi-api" # this represent nifi  adresse that can  be accessed from other docker container throught the external bridge network

topic_liste=[topic_kafka]
consumer=Initiat_Consumers(dic,topic_liste)

Consume_data(consumer,nifi_host)