From python:3.8-slim

WORKDIR /app

COPY requirments.txt /app/

RUN pip install --no-cache-dir -r requirments.txt
ENV broker_hostname=mqtt5 \
    user=user2           \
    password=user2       \
    topic_mqtt=Test1     \
    topic_kafka=test_kafka_1 \
    monitoring_port=9001 \
    kafka_broker=broker:9092


EXPOSE 9001



COPY . /app/

CMD ["python","-u","Consume_mqtt.py"]