From python:3.8-slim

WORKDIR /app

COPY requirments.txt /app/

RUN pip install --no-cache-dir -r requirments.txt
ENV kafka_topic=test_kafka_1
        
COPY . /app/

CMD ["python","-u","Elasticsearch_consume.py"]