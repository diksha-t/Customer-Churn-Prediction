import streamlit as st 
from predictor import predict_customer

st.set_page_config(
    page_title="Customer Churn Prediction",
    layout="wide"
)

st.title("Customer Churn Prediction")

st.write("""
    Predict whether a telecom customer is likely to **churn** using a trained Machine Learning model.
    Fill in the customer information below and click **Predict Churn**.
    """)

st.divider()

st.subheader("Customer Details")
tenure = st.number_input(
        "Tenure(Months)",
        min_value=0,
        max_value=72,
        value=12
    )
monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.35
    )
total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=850.50
    )

st.subheader("Personal Information")
gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)
senior = st.selectbox(
    "Senior Citizen",
    ["No", "Yes"]
)
partner = st.selectbox(
    "Partner",
    ["No", "Yes"]
)
dependents = st.selectbox(
    "Dependents",
    ["No", "Yes"]
)

st.subheader("Phone Services")
phone_service = st.selectbox(
    "Phone Service",
    ["No", "Yes"]
)
multiple_lines = st.selectbox(
    "Multiple Lines",
    [
        "No",
        "Yes",
        "No phone service"
    ]
)

st.subheader("Internet Services")  
internet_service = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

st.subheader("Online Services")
online_security = st.selectbox(
    "Online Security",
    [
        "No",
        "Yes",
        "No internet service"
    ]
)
online_backup = st.selectbox(
    "Online Backup",
    [
        "No",
        "Yes",
        "No internet service"
    ]
)
device_protection = st.selectbox(
    "Device Protection",
    [
        "No",
        "Yes",
        "No internet service"
    ]
)
tech_support = st.selectbox(
    "Tech Support",
    [
        "No",
        "Yes",
        "No internet service"
    ]
)

st.subheader("Streaming")
streaming_tv = st.selectbox(
    "Streaming TV",
    [
        "No",
        "Yes",
        "No internet service"
    ]
)
streaming_movies = st.selectbox(
    "Streaming Movies",
    [
        "No",
        "Yes",
        "No internet service"
    ]
    
)

st.subheader("Billing")
contract = st.selectbox(
        "Contract Type",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )
paperless_billing = st.selectbox(
    "Paperless Billing",
    ["No", "Yes"]
)
payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )
 
st.divider()
predict = st.button(
    "Predict Churn",
    use_container_width=True
)
if predict:
    prediction, probability = predict_customer(
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
    )
    
    st.divider()
    if prediction == 1:
        st.error("Customer is likely to churn.")
    else:
        st.success("Customer is likely to stay.")
        
    st.metric(
        "Churn Probability",
        f"{probability*100:.2f}%"
    )
    
if prediction == 1:

    st.info("""
### Recommendation

• Offer a loyalty discount

• Contact the customer proactively

• Recommend a long-term contract

• Improve customer support
""")

else:

    st.success("""
### 🎉 Recommendation

Customer appears satisfied.

Continue regular engagement and maintain service quality.
""")