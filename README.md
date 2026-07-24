# Customer Churn Prediction & Business Insights

## Project Overview

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn based on customer demographics, services, billing information, and account details.

This project includes data preprocessing, exploratory data analysis, model training, model evaluation, and a Streamlit web application for real-time predictions.

---

## Features

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Logistic Regression model
- StandardScaler preprocessing
- Streamlit web application
- Real-time churn prediction
- Churn probability score
- Customer retention recommendation

---

## Project Structure

```text
Customer Churn Prediction/
│
├── app/
│   ├── app.py
│   ├── predictor.py
│   └── utils.py
│
├── data/
│
├── model/
│   ├── logistic_regression_model.pkl
│   └── standard_scaler.pkl
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_visualization.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_model_building.ipynb
│   └── 05_business_insights.ipynb
│
├── README.md
├── requirements.txt
└── .gitignore
```
---

## Dataset

The project uses the IBM Telco Customer Churn dataset containing customer demographics, account information, services subscribed, billing details and churn status.

---

## Tech Stack

- Python
- Pandas
- Numpy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

---

## Machine Learning Model

Model Used : Logistic Regression
Preprocessing :
- Missing value handling
- One-Hot Encoding
- Feature Scaling using StandardScaler

---

## Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | 80.45% |
| ROC-AUC | 0.843 |
| Precision | 64.02% |
| Recall | 60.43% |
| F1 Score | 62.17% |

---

## Running the Project 

Clone the repo
```bash
git clone
https://github.com/diksha-t/customer-churn-prediction.git
```

Move into the project
```bash
cd customer-churn-prediction
```
Install dependencies
```bash
pip install -r requirements.txt
```

Run the Streamlit app
```bash
streamlit run app/app.py
```
---
 
## Application

This application allows users to:
- Enter customer information
- Predict customer churn
- View churn probability
- Receive retention recommendations

---

## Future Improvements

- Improved UI/UX
- Dockerized application
- Model comparison dashboard
- SHAP Exaplainability
- Feature importance visualization
- Download prediction report
- Batch prediction using CSV upload
