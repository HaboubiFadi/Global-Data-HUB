from confluent_kafka.admin import AdminClient,NewTopic
import socket
from confluent_kafka import Producer

conf = {
    'bootstrap.servers': '127.0.0.1:9092'
}
"""
conf = {
    'bootstrap.servers': 'localhost:9092',
    'max.request.size': 1048576  # Example value, adjust as needed
}
"""
#producer = Producer(conf)

# Retrieve the max.request.size configuration
"""max_request_size = producer.config['max.request.size']

print(f"Max request size for producer: {max_request_size} bytes")"""
topic_config = {"max.message.bytes": 15048576}

topic_list=[]
topic_list.append(NewTopic(
    topic="example_topic",
    num_partitions=1,
    replication_factor=1,
    # replica_assignment=replica_assignment,
    config=topic_config
)
)




admin=AdminClient(conf)

#admin.create_topics(topic_list)
print(admin.list_topics().topics)