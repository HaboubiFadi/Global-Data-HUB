from kafka_functions import Initiat_Consumers,Consume_data

dic={'bootstrap.servers': 'localhost:9092','group.id':'processing_consumer'}
topic_kafka='test_kafka'

topic_liste=[topic_kafka]
consumer=Initiat_Consumers(dic,topic_liste)

Consume_data(consumer)