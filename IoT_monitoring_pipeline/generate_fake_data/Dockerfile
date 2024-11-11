From python:3.8-slim

WORKDIR /app

COPY requirments.txt /app/

RUN pip install --no-cache-dir -r requirments.txt
ENV broker_hostname=mqtt5 \
    user=user2            \
    password=user2         \
    topic=Test1             \
    monitoring_port=9000    \
    interval_time=4         \
    port=1883
    

EXPOSE 9000
COPY script_generate.py /app/

CMD ["python","-u","script_generate.py"]