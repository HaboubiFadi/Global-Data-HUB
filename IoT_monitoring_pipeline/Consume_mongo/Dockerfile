From python:3.8-slim

WORKDIR /app

COPY requirments.txt /app/

RUN pip install --no-cache-dir -r requirments.txt
ENV kafka_topic=test_kafka_1 \
    monitoring_port=9002

EXPOSE 9002

COPY . /app/

CMD ["python","Mongo_consume.py"]