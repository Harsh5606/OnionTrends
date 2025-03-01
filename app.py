import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the trained model and scaler
rf_model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl')

# Streamlit app title
st.title("Onion Price Prediction")

# Input fields for user data
st.header("Enter Input Features")

area = st.number_input("Area (hectares)", min_value=0.0, value=7832.0)
pesticide_usage = st.selectbox("Pesticide Usage", options=[0, 1], format_func=lambda x: "Low" if x == 0 else "High")
ph = st.selectbox("pH Level", options=[0, 1, 2], format_func=lambda x: ["Low", "Average", "High"][x])
temperature = st.selectbox("Temperature", options=[0, 1, 2], format_func=lambda x: ["Low", "Medium", "High"][x])
fertilizer_usage = st.selectbox("Fertilizer Usage", options=[0, 1, 2], format_func=lambda x: ["Low", "Medium", "High"][x])
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, value=3520.7)

# Predict button
if st.button("Predict Price"):
    # Create input data as a DataFrame
    input_data = pd.DataFrame({
        'Area': [area],
        'Pesticide Usage': [pesticide_usage],
        'pH': [ph],
        'Temperature': [temperature],
        'Fertilizer Usage': [fertilizer_usage],
        'Rainfall': [rainfall]
    })

    # Scale the input data using the saved scaler
    input_data_scaled = scaler.transform(input_data)

    # Make a prediction using the Random Forest model
    predicted_price = rf_model.predict(input_data_scaled)

    # Display the predicted price
    st.success(f"Predicted Onion Price: {predicted_price[0]:.2f} INR")
