# data_query.py
import os
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_connection import get_influxdb_client
import pandas as pd

def query_temperature_data(start='-12h'):
    client = get_influxdb_client()
    query_api = client.query_api()

    query = f'''
    from(bucket: "{os.getenv('INFLUXDB_BUCKET')}")
      |> range(start: {start})
      |> filter(fn: (r) => r._measurement == "temp_data")
      |> filter(fn: (r) => r._field == "temperature")
      |> sort(columns: ["_time"], desc: false)
    '''

    tables = query_api.query(query)
    data = []
    for table in tables:
        for record in table.records:
            data.append({
                'time': record.get_time(),
                'value': record.get_value()
            })
    df = pd.DataFrame(data)
    return df
