import joblib

model = joblib.load("../model/logistic_regression_model.pkl")
scaler = joblib.load("../model/standard_scaler.pkl")

FEATURES = [
 'Tenure Months',
 'Monthly Charges',
 'Total Charges',
 'Gender_Male',
 'Senior Citizen_Yes',
 'Partner_Yes',
 'Dependents_Yes',
 'Phone Service_Yes',
 'Multiple Lines_No phone service',
 'Multiple Lines_Yes',
 'Internet Service_Fiber optic',
 'Internet Service_No',
 'Online Security_No internet service',
 'Online Security_Yes',
 'Online Backup_No internet service',
 'Online Backup_Yes',
 'Device Protection_No internet service',
 'Device Protection_Yes',
 'Tech Support_No internet service',
 'Tech Support_Yes',
 'Streaming TV_No internet service',
 'Streaming TV_Yes',
 'Streaming Movies_No internet service',
 'Streaming Movies_Yes',
 'Contract_One year',
 'Contract_Two year',
 'Paperless Billing_Yes',
 'Payment Method_Credit card (automatic)',
 'Payment Method_Electronic check',
 'Payment Method_Mailed check'
]

import pandas as pd

def predict_customer(
    tenure,
    monthly_charges,
    total_charges,
    gender,
    senior,
    partner,
    dependents,
    phone_service,
    multiple_lines,
    internet_service,
    online_security,
    online_backup,
    device_protection,
    tech_support,
    streaming_tv,
    streaming_movies,
    contract,
    paperless_billing,
    payment_method
):
    data = {feature: 0 for feature in FEATURES}
    data["Tenure Months"] = tenure
    data["Monthly Charges"] = monthly_charges
    data["Total Charges"] = total_charges
    
    if gender == "Male":
        data["Gender_Male"] = 1
    
    if senior == "Yes":
        data["Senior_Citizen_Yes"] = 1
    
    if partner == "Yes":
        data["Partner_Yes"] = 1
        
    if dependents == "Yes":
        data["Dependents_Yes"] = 1
        
    if phone_service == "Yes":
        data["Phone Service_Yes"] = 1
        
    if paperless_billing == "Yes":
        data["Paperless Billing_Yes"] = 1