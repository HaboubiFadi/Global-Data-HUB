FROM python:3.8-slim

WORKDIR /app

COPY requirments.txt /app/

RUN pip install --no-cache-dir -r requirments.txt

EXPOSE 5000

COPY . /app/

CMD ["python","-u","publish_api_endpoint.py"] 