from dash import Dash, dcc, html
import plotly.express as px
import requests
import pandas as pd
from io import StringIO

# Initialize the Dash app
app = Dash(__name__)

# Fetch data from Flask API
def fetch_data(url, required_columns):
    response = requests.get(url)
    if response.status_code == 200:
        data = pd.read_json(StringIO(response.text))
        print(f"Data fetched from {url}:")
        print(data.head())
        return data
    else:
        print(f"Failed to fetch data from {url}")
        return pd.DataFrame(columns=required_columns)  # Return an empty DataFrame with required columns

fraud_summary = requests.get('http://localhost:5000/fraud_data').json()
fraud_trends = fetch_data('http://localhost:5000/fraud_trends', ['date', 'fraud_cases'])
fraud_geography = fetch_data('http://localhost:5000/fraud_geography', ['country', 'fraud_cases'])
fraud_devices = fetch_data('http://localhost:5000/fraud_devices', ['device', 'fraud_cases'])
fraud_browsers = fetch_data('http://localhost:5000/fraud_browsers', ['browser', 'fraud_cases'])

# Convert date column to datetime
if not fraud_trends.empty:
    fraud_trends['date'] = pd.to_datetime(fraud_trends['date']).dt.to_pydatetime()

# Create figures with checks for empty DataFrames
geography_figure = (
    px.choropleth(
        fraud_geography,
        locations='country',
        locationmode='country names',
        color='fraud_cases',
        title='Fraud Cases by Country'
    ) if not fraud_geography.empty and 'country' in fraud_geography.columns else px.choropleth(title='No Data Available for Fraud Geography')
)

devices_figure = (
    px.bar(
        fraud_devices,
        x='device',
        y='fraud_cases',
        title='Fraud Cases by Device'
    ) if not fraud_devices.empty and 'device' in fraud_devices.columns else px.bar(title='No Data Available for Fraud Devices')
)

# Layout of the Dash app
app.layout = html.Div(children=[
    html.H1(children='Fraud Detection Dashboard'),

    html.Div(children=[
        html.Div(children=[
            html.H3(children='Total Transactions'),
            html.P(children=f"{fraud_summary['total_transactions']}")
        ], className='summary-box'),

        html.Div(children=[
            html.H3(children='Total Fraud Cases'),
            html.P(children=f"{fraud_summary['total_fraud_cases']}")
        ], className='summary-box'),

        html.Div(children=[
            html.H3(children='Fraud Percentage'),
            html.P(children=f"{fraud_summary['fraud_percentage']:.2f}%")
        ], className='summary-box'),
    ], className='summary-container'),

    dcc.Graph(
        id='fraud-trends',
        figure=px.line(fraud_trends, x='date', y='fraud_cases', title='Fraud Cases Over Time')
    ),

    dcc.Graph(
        id='fraud-geography',
        figure=geography_figure
    ),

    dcc.Graph(
        id='fraud-devices',
        figure=devices_figure
    ),

    dcc.Graph(
        id='fraud-browsers',
        figure=px.bar(fraud_browsers, x='browser', y='fraud_cases', title='Fraud Cases by Browser')
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)