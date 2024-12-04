# app.py
import os, time
from influxdb_client_3 import InfluxDBClient3, Point
import streamlit as st
import pandas as pd
import plotly.express as px
#from data_query import query_temperature_data
from dotenv import load_dotenv
from streamlit_autorefresh import st_autorefresh

load_dotenv()



st.set_page_config(
    page_title="Real-Time Temperature Monitoring",
    layout="wide",
)

st.title("🌡️ Real-Time Temperature Monitoring")

# Sidebar for user input
start_time = st.sidebar.selectbox(
    "Select Time Range",
    options=['-15m', '-30m', '-1h', '-6h', '-12h', '-24h'],
    index=2
)

st.sidebar.markdown("Data refreshes every 5 seconds.")

# Placeholder for the chart
chart_placeholder = st.empty()

# Display current temperature
latest_temp_placeholder = st.empty()

# Autorefresh every REFRESH_RATE milliseconds
REFRESH_RATE = 5 * 1000  # milliseconds

st_autorefresh(interval=REFRESH_RATE, key="datarefresh")

def render_chart():
    host = os.getenv('INFLUXDB_URL')
    token = os.getenv('INFLUXDB_TOKEN')
    org = os.getenv('INFLUXDB_ORG')
    client = InfluxDBClient3(host=host, token=token, org=org)
    query = """SELECT *
        FROM 'temp_data'
        WHERE time >= now() - interval '24 hours'
        """

    # Execute the query
    table = client.query(query=query, database="sensor_data", language='sql')

    # Convert to dataframe
    df = table.to_pandas().sort_values(by="time")
    #print(df)
    st.dataframe(df)
 

render_chart()
