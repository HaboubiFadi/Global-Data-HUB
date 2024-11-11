from kafka_functions import Initiat_Consumers,Consume_data_mongo
import os
from mongo import mongo_instance
from prometheus_client.core import Gauge, Counter
from prometheus_client import start_http_server
dic={'bootstrap.servers': 'broker:9092','group.id':'Mongodb_team'}


topic_kafka=os.environ.get("kafka_topic") # Environement variable   
monitoring_port=os.environ.get('monitoring_port')

#server="http://mongo:9200"
start_http_server(int(monitoring_port))

mg_instance=mongo_instance()

topic_liste=[topic_kafka]
consumer=Initiat_Consumers(dic,topic_liste)
db_name='Test'
db_collection='test1'
monitoring_var=''
Consume_data_mongo(mg_instance,db_name,db_collection,consumer)
