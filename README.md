# Fraud Detection System

## Project Overview
This project aims to improve fraud detection for e-commerce and bank credit transactions using advanced machine learning models. The goal is to enhance security, minimize financial losses, and ensure trust in financial transactions.

## Business Objective
Fraud detection is critical for preventing unauthorized transactions and securing financial systems. This project leverages geolocation analysis and transaction pattern recognition to build an effective fraud detection system.

## Features
- **Data Preprocessing:** Handling missing values, data cleaning, and encoding categorical variables.
- **Exploratory Data Analysis (EDA):** Understanding transaction patterns and fraud trends.
- **Feature Engineering:** Creating transaction frequency, velocity, and time-based features.
- **Machine Learning Models:** Training models to detect fraudulent transactions accurately.
- **API Development:** Deploying the fraud detection model using Flask.
- **Containerization:** Dockerizing the application for scalable deployment.
- **Dashboard Development:** Visualizing fraud insights using Dash.

## Technologies Used
- Python (Pandas, NumPy, Scikit-learn, Matplotlib, Flask, Dash)
- SQL for data storage and retrieval
- Docker for containerization
- GitHub for version control and CI/CD

## Dataset Description
- **Fraud_Data.csv:** E-commerce transaction records with fraud labels.
- **IpAddress_to_Country.csv:** Maps IP addresses to their respective countries.
- **creditcard.csv:** Bank transaction data with anonymized PCA-transformed features.

## Setup Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/Kifiya-AIM-Week-8.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Kifiya-AIM-Week-8
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the data preprocessing script:
   ```bash
   python preprocess.py
   ```
5. Train the model:
   ```bash
   python train_model.py
   ```
6. Start the Flask API:
   ```bash
   python app.py
   ```

## Contribution Guidelines
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature-branch
   ```
5. Submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For questions or contributions, contact: tewodroshabtamu29@gmail.com or create an issue in this repository.
