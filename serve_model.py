from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px

app = Flask(__name__)

# Load the saved models
fraud_model = joblib.load("./notebooks/models/fraud_random_forest.joblib")
credit_model = joblib.load("./notebooks/models/credit_random_forest.joblib")

@app.route('/predict_fraud', methods=['POST'])
def predict_fraud():
    data = request.get_json(force=True)
    features = np.array(data['features']).reshape(1, -1)
    prediction = fraud_model.predict(features)
    return jsonify({'prediction': int(prediction[0])})

@app.route('/predict_credit', methods=['POST'])
def predict_credit():
    data = request.get_json(force=True)
    features = np.array(data['features']).reshape(1, -1)
    prediction = credit_model.predict(features)
    return jsonify({'prediction': int(prediction[0])})

@app.route('/fraud_data', methods=['GET'])
def fraud_data():
    df = pd.read_csv('./data/Fraud_Data.csv')
    summary = {
        'total_transactions': len(df),
        'total_fraud_cases': df['class'].sum(),
        'fraud_percentage': df['class'].mean() * 100
    }
    return jsonify(summary)

@app.route('/fraud_trends', methods=['GET'])
def fraud_trends():
    df = pd.read_csv('./data/Fraud_Data.csv')
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])
    trends = df.groupby(df['purchase_time'].dt.date)['class'].sum().reset_index()
    trends.columns = ['date', 'fraud_cases']
    return trends.to_json(orient='records')

# Initialize the Dash app
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/dashboard/')

# Fetch data from Flask API
fraud_summary = requests.get('http://localhost:5000/fraud_data').json()
fraud_trends = pd.read_json(requests.get('http://localhost:5000/fraud_trends').text)

# Layout of the Dash app
dash_app.layout = html.Div(children=[
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
    app.run(host='0.0.0.0', port=5000)