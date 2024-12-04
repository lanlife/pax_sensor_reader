# influxdb_connection.py
import os
from influxdb_client import InfluxDBClient

def get_influxdb_client():
    url = os.getenv('INFLUXDB_URL')
    token = os.getenv('INFLUXDB_TOKEN')
    org = os.getenv('INFLUXDB_ORG')
    client = InfluxDBClient(url=url, token=token, org=org)
    return client
