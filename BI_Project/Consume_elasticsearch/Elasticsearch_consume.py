from kafka_functions import Initiat_Consumers,Consume_data_elasticsearch
import os
from Elasticsearch import Elasticsearch_instance
dic={'bootstrap.servers': 'broker:9092','group.id':'Elasticsearch_team'}

topic_kafka=os.environ.get("kafka_topic") # Environement variable   

server="http://elasticsearch:9200"

index_name='test_bi'

elastic_instance=Elasticsearch_instance(server)
elastic_instance.create_index(index_name)


topic_liste=[topic_kafka]
consumer=Initiat_Consumers(dic,topic_liste)

Consume_data_elasticsearch(elastic_instance,index_name,consumer)
