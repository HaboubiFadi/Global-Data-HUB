import time
import json
from confluent_kafka import Producer
from tools import generate_vehicule_and_shipment

# Kafka configuration
kafka_config = {
    'bootstrap.servers': 'broker:9092',  
    'client.id': 'test_client'}
topic = 'test_topic'  

producer = Producer(kafka_config)

time.sleep(10)

def produce_json():
    try:
        num_vehicles=10
        num_months=6
        num_shipments=100
        claim_percentage=0.3

        
        pre_json=generate_vehicule_and_shipment(num_vehicles,num_months,num_shipments,claim_percentage)
        print(pre_json[-1].keys())
        producer.produce(topic, key=None, value=json.dumps(pre_json))
        producer.flush()  
        print(f'Produced json  to topic {topic}')
    except Exception as e:
        print(f'Failed to produce json : {e}')


# Produce the file every 10 seconds
while True:
    produce_json()
    time.sleep(400)  
