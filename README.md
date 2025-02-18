
# Fraud Detection System for E-commerce and Banking Transactions

## Overview

This repository contains the code and resources for building a robust fraud detection system tailored for e-commerce and banking transactions. The project leverages advanced machine learning models, geolocation analysis, and transaction pattern recognition to improve the accuracy of fraud detection. The system is designed to enhance transaction security, prevent financial losses, and build trust with customers and financial institutions.

## Business Need

Adey Innovations Inc., a leading company in the financial technology sector, aims to improve the detection of fraudulent activities in e-commerce and bank credit transactions. By utilizing advanced machine learning techniques and detailed data analysis, this project seeks to create accurate and reliable fraud detection models that can handle the unique challenges of both types of transaction data.

## Datasets

The project utilizes the following datasets:

1. Fraud_Data.csv: Contains e-commerce transaction data aimed at identifying fraudulent activities.

   - `user_id`: Unique identifier for the user.
   - `signup_time`: Timestamp when the user signed up.
   - `purchase_time`: Timestamp when the purchase was made.
   - `purchase_value`: Value of the purchase in dollars.
   - `device_id`: Unique identifier for the device used.
   - `source`: Source through which the user came to the site (e.g., SEO, Ads).
   - `browser`: Browser used to make the transaction (e.g., Chrome, Safari).
   - `sex`: Gender of the user (M for male, F for female).
   - `age`: Age of the user.
   - `ip_address`: IP address from which the transaction was made.
   - `class`: Target variable where 1 indicates a fraudulent transaction and 0 indicates a non-fraudulent transaction.

2. IpAddress_to_Country.csv: Maps IP addresses to countries.

   - `lower_bound_ip_address`: Lower bound of the IP address range.
   - `upper_bound_ip_address`: Upper bound of the IP address range.
   - `country`: Country corresponding to the IP address range.

3. creditcard.csv: Contains bank transaction data specifically curated for fraud detection analysis.
   - `Time`: Number of seconds elapsed between this transaction and the first transaction in the dataset.
   - `V1 to V28`: Anonymized features resulting from a PCA transformation.
   - `Amount`: Transaction amount in dollars.
   - `Class`: Target variable where 1 indicates a fraudulent transaction and 0 indicates a non-fraudulent transaction.

## Project Tasks

### Task 1 - Data Analysis and Preprocessing

- Handle Missing Values: Impute or drop missing values.
- Data Cleaning: Remove duplicates and correct data types.
- Exploratory Data Analysis (EDA): Perform univariate and bivariate analysis.
- Merge Datasets for Geolocation Analysis: Convert IP addresses to integer format and merge `Fraud_Data.csv` with `IpAddress_to_Country.csv`.
- Feature Engineering: Create features such as transaction frequency, velocity, and time-based features (e.g., hour_of_day, day_of_week).
- Normalization and Scaling: Normalize and scale the data.
- Encode Categorical Features: Encode categorical variables for model training.

### Task 2 - Model Building and Training

- Data Preparation: Separate features and target variables (`Class` for creditcard, `class` for Fraud_Data) and perform train-test split.
- Model Selection: Compare performance of various models including Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, Multi-Layer Perceptron (MLP), Convolutional Neural Network (CNN), Recurrent Neural Network (RNN), and Long Short-Term Memory (LSTM).
- Model Training and Evaluation: Train models for both datasets and evaluate their performance.
- MLOps Steps: Use tools like MLflow for versioning and experiment tracking.

Teddy 🌱SEED, [2/18/25 8:24 PM]

### Task 3 - Model Explainability

- Using SHAP for Explainability: Install SHAP and use it to explain model predictions with summary plots, force plots, and dependence plots.
- Using LIME for Explainability: Install LIME and use it to explain individual predictions with feature importance plots.

### Task 4 - Model Deployment and API Development

- Setting Up the Flask API: Create a Flask application to serve the model.
- API Development: Define API endpoints and test the API.
- Dockerizing the Flask Application: Create a Dockerfile to containerize the Flask application.
- Build and Run the Docker Container: Build the Docker image and run the container.

### Task 5 - Build a Dashboard with Flask and Dash

- Create an Interactive Dashboard: Use Dash for frontend visualizations and Flask for backend data serving.
- Dashboard Insights: Display total transactions, fraud cases, fraud percentages, line charts for fraud trends over time, geographic analysis of fraud, and bar charts comparing fraud cases across devices and browsers.

## Deliverables

- Data Analysis and Preprocessing: Cleaned and preprocessed datasets ready for model training.
- Model Building and Training: Trained machine learning models with evaluation metrics.
- Model Explainability: SHAP and LIME plots for model interpretability.
- Model Deployment: Flask API for real-time fraud detection and Docker container for deployment.
- Dashboard: Interactive dashboard for visualizing fraud insights.

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fraud-detection-system.git
   cd fraud-detection-system
   ```
2. Install the required dependencies:

```bash
 pip install -r requirements.txt
```

3. Run the Flask API:

```bash
 python serve_model.py
```

4. Build and run the Docker container:

```bash
 docker build -t fraud-detection-model .
 docker run -p 5000:5000 fraud-detection-model
```

## Usage

- API Endpoints: Access the API endpoints to get real-time fraud predictions.
- Dashboard: Navigate to the dashboard to visualize fraud insights and trends.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Adey Innovations Inc. for providing the datasets and business context.
- The open-source community for providing tools and libraries used in this project.

`
