# influxdb_connection.py
import os
from influxdb_client_3 import InfluxDBClient3, Point

def get_influxdb_client():
    host = os.getenv('INFLUXDB_URL')
    token = os.getenv('INFLUXDB_TOKEN')
    org = os.getenv('INFLUXDB_ORG')
    client = InfluxDBClient3(host=host, token=token, org=org)
    
    return client
