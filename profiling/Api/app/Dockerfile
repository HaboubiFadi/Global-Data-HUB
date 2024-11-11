FROM python:3.10.2

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt
        
COPY . /app/

EXPOSE 800

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","800"]