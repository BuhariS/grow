import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("mymodel.pkl")

st.title("Taxi Fare Prediction App")

# User inputs
passenger_count = st.number_input("Passenger Count")
distance_km = st.number_input("Distance in KM")
hour = st.number_input("Hour")
month = st.number_input("Month")
day_of_week = st.number_input("Day of Week")

# Prediction button
if st.button("Predict"):
    features = pd.DataFrame({
        
        "passenger_count": [passenger_count],
        "hour": [hour],
        "day_of_week": [day_of_week],
        "month": [month],
        "distance_km": [distance_km],
        
        
    })

    prediction = model.predict(features)

    st.success(f"Predicted Value: {prediction[0]}")