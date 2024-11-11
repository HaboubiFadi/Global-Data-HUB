from fastapi import FastAPI
from typing import List
from pymongo import MongoClient
import strawberry
from strawberry.asgi import GraphQL


var_types=[['Adresse','s',30],['Mileage','int',8],['Fuel_level','reel',100],['Speed','reel',300],['Longitude','reel',180]]


app = FastAPI()
db_name='Test'
db_collection='test1'

client = MongoClient("mongodb://admin:admin@localhost:27017")
db = client[db_name]
collection = db[db_collection]
@strawberry.type
class IoT:
    _id:str
    Adresse: str
    Mileage: int
    Fuel_level:float
    Speed:float
    Longitude:float

@strawberry.type
class Query:
    @strawberry.field
    def IoTs(self) -> List[IoT]:
        Iots = []
        for ioT in collection.find():
            try:
                print(ioT)
                iot_device = IoT(**ioT)
                Iots.append(iot_device)
            except Exception as e:
                print('Error',e)
                pass    
        return Iots

    @strawberry.field
    def IoT(self, Speed: float) -> IoT:
        Iot_col = collection.find_one({"Speed": Speed})
        try:
            if Iot_col:
                return IoT(**Iot_col)
            else:
                return None    
        except:
            print('Error')    

schema = strawberry.Schema(query=Query)
app.mount("/graphql", GraphQL(schema, debug=True))


# uvicorn main:app --reload Command run uvicorn server and the fastapi server