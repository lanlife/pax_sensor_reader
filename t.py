import os, time
from influxdb_client_3 import InfluxDBClient3, Point

token = os.environ.get("INFLUXDB_TOKEN")
org = "Stage Test"
host = "https://eu-central-1-1.aws.cloud2.influxdata.com"

client = InfluxDBClient3(host=host, token=token, org=org)

query = """SSELECT *
FROM "temp_data"
WHERE
time >= now() - interval '12 hours'
"""

# Execute the query
table = client.query(query=query, database="sensor_data", language='sql')

# Convert to dataframe
df = table.to_pandas().sort_values(by="time")
print(df)
