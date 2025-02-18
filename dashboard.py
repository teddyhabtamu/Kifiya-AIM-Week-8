import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px
import requests
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)

# Fetch data from Flask API
fraud_summary = requests.get('http://localhost:5000/fraud_data').json()
fraud_trends = pd.read_json(requests.get('http://localhost:5000/fraud_trends').text)

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

    # Add more visualizations here
])

if __name__ == '__main__':
    app.run_server(debug=True)