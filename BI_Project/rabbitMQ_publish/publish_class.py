import pika 


class Publisher():
    def __init__(self,config):
        self.config=config

    def Create_connection(self):
        credentials = pika.PlainCredentials('fadi1', 'fadi1')
        param=pika.ConnectionParameters(host=self.config['host'],port=self.config['port'],credentials=credentials)
        return pika.BlockingConnection(param)

    def Publish(self,routing_key,message):
        connection = self.Create_connection()   
        channel=connection.channel()
        channel.exchange_declare(exchange=self.config["exchange"],exchange_type="topic")
        print(channel.basic_publish(exchange=self.config["exchange"],routing_key=routing_key, body=message))


