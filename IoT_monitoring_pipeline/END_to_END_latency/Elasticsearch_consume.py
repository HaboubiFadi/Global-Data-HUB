from kafka_functions import Initiat_Consumers,Consume_data
import os
dic={'bootstrap.servers': 'broker:9092','group.id':'test_team'}

topic_kafka=os.environ.get("kafka_topic") # Environement variable   





topic_liste=[topic_kafka]
consumer=Initiat_Consumers(dic,topic_liste)

Consume_data(consumer)
