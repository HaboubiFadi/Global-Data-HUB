from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import connection
from cassandra.cluster import Cluster
class MyModel(Model):
    id = columns.Integer(primary_key=True)
    name = columns.Text()
    age = columns.Integer()