from kafka_functions import Initiat_Consumers,Consume_data_cassandra
import os
from Cassandra import Cassandra_instance
from IoT_instance import IoT_instance
dic={'bootstrap.servers': 'broker:9092','group.id':'cassandra_team'}

topic_kafka=os.environ.get("kafka_topic") # Environement variable   

server=['cas']
keyspace=os.environ.get('keyspace')


cassandra_instance=Cassandra_instance(server,keyspace)


topic_liste=[topic_kafka]

consumer=Initiat_Consumers(dic,topic_liste)

Consume_data_cassandra(cassandra_instance,IoT_instance,consumer)
