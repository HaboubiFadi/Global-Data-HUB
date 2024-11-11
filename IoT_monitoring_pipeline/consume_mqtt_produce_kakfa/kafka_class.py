
from confluent_kafka import Producer,Consumer

class Singleton_kafka_producer(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(Singleton_kafka_producer, cls).__new__(cls)
    return cls.instance
  
  def initiate(self,configuration_server,topic):
        self.producer = Producer(configuration_server)
        self.topic=topic
  
  def produce(self,key,value):
        
    self.producer.produce(self.topic, key=str(key), value=value)
    self.producer.flush()
    
  def Serialization(DataFrame):
    return DataFrame.to_json()
    

