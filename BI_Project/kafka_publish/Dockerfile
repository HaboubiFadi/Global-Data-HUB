From python:3.8-slim

WORKDIR /app

COPY requirments.txt /app/

RUN pip install --no-cache-dir -r requirments.txt
        
COPY . /app/

CMD ["python","-u","kafka_produce.py"]