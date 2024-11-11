From python:3.8-slim

WORKDIR /app

COPY requirments.txt /app/

RUN pip install --no-cache-dir -r requirments.txt
ENV broker_hostname=mqtt5 \
    user=user2           \
    password=user2       \
    monitoring_port=9000

EXPOSE 9000



COPY . /app/

CMD ["python","-u","exporter_script.py"]