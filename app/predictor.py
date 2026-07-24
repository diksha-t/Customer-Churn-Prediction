import joblib
import pandas as pd

model = joblib.load("model/logistic_regression_model.pkl")
scaler = joblib.load("model/standard_scaler.pkl")

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
        data["Senior Citizen_Yes"] = 1
    
    if partner == "Yes":
        data["Partner_Yes"] = 1
        
    if dependents == "Yes":
        data["Dependents_Yes"] = 1
        
    if phone_service == "Yes":
        data["Phone Service_Yes"] = 1
        
    if paperless_billing == "Yes":
        data["Paperless Billing_Yes"] = 1
        
    if multiple_lines == "Yes":
        data["Multiple Lines_Yes"] = 1
    elif multiple_lines == "No phone service":
        data["Multiple Lines_No phone service"] = 1
        
    if internet_service == "Fiber optic":
        data["Internet Service_Fiber optic"] = 1
    elif internet_service == "No":
        data["Internet Service_No"] = 1
        
    if online_security == "Yes":
        data["Online Security_Yes"] = 1
    elif online_security == "No internet service":
        data["Online Security_No internet service"] = 1
        
    if online_backup == "Yes":
        data["Online Backup_Yes"] = 1
    elif online_backup == "No internet service":
        data["Online Backup_No internet service"] = 1
        
    if device_protection == "Yes":
        data["Device Protection_Yes"] = 1
    elif device_protection == "No internet service":
        data["Device Protection_No internet service"] = 1
        
    if tech_support == "Yes":
        data["Tech Support_Yes"] = 1
    elif tech_support == "No internet service":
        data["Tech Support_No internet service"] = 1
        
    if streaming_movies == "Yes":
        data["Streaming Movies_Yes"] = 1
    elif streaming_movies == "No internet service":
        data["Streaming Movies_No internet service"] = 1
        
    if contract == "One year":
        data["Contract_One year"] = 1
    elif contract == "Two year":
        data["Contract_Two year"] = 1
        
    if payment_method == "Electronic check":
        data["Payment Method_Electronic check"] = 1
    elif payment_method == "Mailed check":
        data["Payment Method_Mailed check"] = 1
    elif payment_method == "Credit card (automatic)":
        data["Payment Method_Credit card (automatic)"] = 1
        
# converting dictionary to dataframe, for the model
    df = pd.DataFrame([data])
    df[["Tenure Months", "Monthly Charges", "Total Charges"]] = scaler.transform(df[["Tenure Months", "Monthly Charges", "Total Charges"]]
    )

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]
    return prediction, probability