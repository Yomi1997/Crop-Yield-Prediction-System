# main.py  (Streamlit version of your Flask app)

import streamlit as st
import pickle
import numpy as np

# 🔹 Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# 🚀 Streamlit UI
st.title("🌱 Crop Prediction App")

# Input fields (replacing JSON request)
N = st.number_input("Nitrogen (N)", min_value=0, max_value=200, value=90)
P = st.number_input("Phosphorus (P)", min_value=0, max_value=200, value=40)
K = st.number_input("Potassium (K)", min_value=0, max_value=200, value=40)
temp = st.number_input("Temperature (°C)", min_value=-10.0, max_value=60.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, value=70)
ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=200.0)

if st.button("Predict Crop"):
    try:
        # Prepare features
        features = [N, P, K, temp, humidity, ph, rainfall]

        # Prediction
        prediction = model.predict([np.array(features)])
        predicted_crop = prediction[0]

        st.success(f"🌾 Predicted Crop: {predicted_crop}")

    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
