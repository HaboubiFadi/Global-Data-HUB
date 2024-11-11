
from confluent_kafka import Producer,Consumer
dic={'bootstrap.servers': 'broker:9092'}

class Singleton_kafka_producer(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(Singleton_kafka_producer, cls).__new__(cls)
    return cls.instance
  
  def initiate(self,configuration_server,topic):
        self.producer = Producer(configuration_server)
        self.topic=topic
  def produce(self,key,value):
    print('/n data_key:',key)
        
    self.producer.produce(self.topic, key=key, value=value)
    self.producer.flush()
    
  def Serialization(DataFrame):
    return DataFrame.to_json()
    

