# streamlit_app.py

import streamlit as st
import pickle
import numpy as np

# 🔹 Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# 🔹 Streamlit App
st.title("Crop Prediction App 🌱")
st.write("Enter the values below to predict the suitable crop:")

# Input fields
N = st.number_input("Nitrogen (N)", min_value=0.0, step=1.0)
P = st.number_input("Phosphorus (P)", min_value=0.0, step=1.0)
K = st.number_input("Potassium (K)", min_value=0.0, step=1.0)
temp = st.number_input("Temperature (°C)", min_value=-50.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, step=0.1)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=0.1)

# Prediction button
if st.button("Predict Crop"):
    try:
        features = [N, P, K, temp, humidity, ph, rainfall]
        prediction = model.predict([np.array(features)])
        st.success(f"🌾 Predicted Crop: {prediction[0]}")
    except Exception as e:
        st.error(f"Error: {str(e)}")
