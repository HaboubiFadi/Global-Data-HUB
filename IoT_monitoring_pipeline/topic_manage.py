from confluent_kafka.admin import AdminClient,NewTopic
import socket
from confluent_kafka import Producer


conf = {
    'bootstrap.servers': 'localhost:9092'
}
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

admin.create_topics(topic_list)
print(admin.list_topics().topics)


"""logging:
      driver: syslog
      options:
        syslog-address: "tcp://localhost:5044"""
