from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import connection
from cassandra.cluster import Cluster
import uuid


class IoT_instance(Model):
    id      = columns.UUID(primary_key=True, default=uuid.uuid4)
    Adresse    = columns.Text(required=False)
    Mileage    = columns.Integer(index=True)
    Fuel_level    = columns.Float(index=True)
    Speed    = columns.Float(index=True)
    Longitude    = columns.Float(index=True)
    
    Timestamp      = columns.DateTime()
