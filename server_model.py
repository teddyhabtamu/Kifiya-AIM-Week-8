from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the saved models
fraud_model = joblib.load("fraud_random_forest.joblib")
credit_model = joblib.load("credit_random_forest.joblib")

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)