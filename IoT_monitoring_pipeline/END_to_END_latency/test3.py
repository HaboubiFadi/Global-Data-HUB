import docker
client = docker.from_env()
print(client.containers.list())

"""
container = client.containers.get('generate_image_2')
container4 = client.containers.get('pfe_generate_image')

container1 = client.containers.get('pfe_consume_mqtt_1')
container2 = client.containers.get('pfe_consume_kafka_mongo_1')"""


#containers=[container,container1,container2,container4]


list_containers_name=['generate_image','pfe_consume_mqtt','consume_kafka_mongo']

def match_string_liste(string,liste):
    for item in liste:
        if item in string:
            return True
    return False    
def Get_required_containers(list_containers_name):
    active_containers_liste=client.containers.list()
    containers_list_required=[]
    print(client.containers.list())
    for container in active_containers_liste:
        if match_string_liste(container.name ,list_containers_name):
            print(container.name)
            containers_list_required.append(container)
    return  containers_list_required       



liste=Get_required_containers(list_containers_name)
print(liste)


"""
kafka_connect :
    image :  kafka_connect
    container_name: kafka_connect_mqtt
    depends_on:
      - zookeeper
      - broker
    ports:
      - 8083:8083

    environment:
      CONNECT_BOOTSTRAP_SERVERS: "broker:9092"
      CONNECT_GROUP_ID: compose-connect-group
      CONNECT_CONFIG_STORAGE_TOPIC: docker-connect-configs
      CONNECT_OFFSET_STORAGE_TOPIC: docker-connect-offsets
      CONNECT_STATUS_STORAGE_TOPIC: docker-connect-status
      CONNECT_CONFIG_STORAGE_REPLICATION_FACTOR: 1
      CONNECT_OFFSET_STORAGE_REPLICATION_FACTOR: 1
      CONNECT_STATUS_STORAGE_REPLICATION_FACTOR: 1
      CONNECT_KEY_CONVERTER: "org.apache.kafka.connect.json.JsonConverter"
      CONNECT_VALUE_CONVERTER: "org.apache.kafka.connect.json.JsonConverter"
      CONNECT_INTERNAL_KEY_CONVERTER: "org.apache.kafka.connect.json.JsonConverter"
      CONNECT_INTERNAL_VALUE_CONVERTER: "org.apache.kafka.connect.jsosn.JsonConverter"
      CONNECT_REST_PORT: 8083
      CONNECT_REST_ADVERTISED_HOST_NAME: "kafka-connect"  
    networks: 
      - kafka
"""