from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the saved models
fraud_model = joblib.load("./notebooks/models/fraud_decision_tree.joblib")
credit_model = joblib.load("./notebooks/models/credit_decision_tree.joblib")

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
    df = pd.read_csv('./assets/Data/Fraud_Data.csv')
    summary = {
        'total_transactions': int(len(df)),
        'total_fraud_cases': int(df['class'].sum()),
        'fraud_percentage': float(df['class'].mean() * 100)
    }
    return jsonify(summary)

@app.route('/fraud_trends', methods=['GET'])
def fraud_trends():
    df = pd.read_csv('./assets/Data/Fraud_Data.csv')
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])
    trends = df.groupby(df['purchase_time'].dt.date)['class'].sum().reset_index()
    trends.columns = ['date', 'fraud_cases']
    return trends.to_json(orient='records')

@app.route('/fraud_geography', methods=['GET'])
def fraud_geography():
    df = pd.read_csv('./assets/Data/Fraud_Data.csv')
    print("DataFrame head for fraud_geography endpoint:")
    print(df.head())
    geography = df.groupby('country')['class'].sum().reset_index()
    geography.columns = ['country', 'fraud_cases']
    print("Geography DataFrame:")
    print(geography.head())
    return geography.to_json(orient='records')

@app.route('/fraud_devices', methods=['GET'])
def fraud_devices():
    df = pd.read_csv('./assets/Data/Fraud_Data.csv')
    print("DataFrame head for fraud_devices endpoint:")
    print(df.head())
    devices = df.groupby('device')['class'].sum().reset_index()
    devices.columns = ['device', 'fraud_cases']
    print("Devices DataFrame:")
    print(devices.head())
    return devices.to_json(orient='records')

@app.route('/fraud_browsers', methods=['GET'])
def fraud_browsers():
    df = pd.read_csv('./assets/Data/Fraud_Data.csv')
    browsers = df.groupby('browser')['class'].sum().reset_index()
    browsers.columns = ['browser', 'fraud_cases']
    return browsers.to_json(orient='records')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)