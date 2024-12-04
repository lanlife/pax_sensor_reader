# data_query.py
import os, time
from influxdb_client_3 import InfluxDBClient3, Point

import pandas as pd

def query_temperature_data(start='-12h'):
    query = """SELECT *
    FROM 'temp_data'
    WHERE time >= now() - interval '24 hours'
    """

    # Execute the query
    table = client.query(query=query, database="sensor_data", language='sql')

    # Convert to dataframe
    df = table.to_pandas().sort_values(by="time")
    #print(df)
    return df

