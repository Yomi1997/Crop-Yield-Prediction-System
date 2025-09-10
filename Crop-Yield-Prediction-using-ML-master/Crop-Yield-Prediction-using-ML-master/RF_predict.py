# streamlit_rf_predict.py

import streamlit as st
import pickle
import numpy as np
import requests

# 🔹 OpenWeatherMap API key
api_key = "95348aea3125b4e8881f126ab8cb646b"

# 🔹 Load trained ML model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# 🔹 Streamlit App
st.title("Crop Yield & Prediction App 🌱")
st.write("Enter the details below to predict the crop and estimated yield:")

# Inputs
district = st.text_input("District / State")
crop = st.text_input("Crop Name")
area = st.number_input("Area (Acres)", min_value=0.1, step=0.1)

soil = st.selectbox("Soil Type", ["Loamy", "Sandy", "Clay"]).lower()

# Soil NPK + pH values
defined_soils = {
    "loamy":  {"N": 90, "P": 40, "K": 40, "ph": 6.5},
    "sandy":  {"N": 60, "P": 30, "K": 35, "ph": 5.8},
    "clay":   {"N": 75, "P": 45, "K": 50, "ph": 6.8}
}

# Nigerian states mapped to capitals
fallback_cities = {
    "Abia": "Umuahia", "Adamawa": "Yola", "Akwa Ibom": "Uyo", "Anambra": "Awka",
    "Bauchi": "Bauchi", "Bayelsa": "Yenagoa", "Benue": "Makurdi", "Borno": "Maiduguri",
    "Cross River": "Calabar", "Delta": "Asaba", "Ebonyi": "Abakaliki", "Edo": "Benin City",
    "Ekiti": "Ado-Ekiti", "Enugu": "Enugu", "FCT": "Abuja", "Gombe": "Gombe",
    "Imo": "Owerri", "Jigawa": "Dutse", "Kaduna": "Kaduna", "Kano": "Kano",
    "Katsina": "Katsina", "Kebbi": "Birnin Kebbi", "Kogi": "Lokoja", "Kwara": "Ilorin",
    "Lagos": "Ikeja", "Nasarawa": "Lafia", "Niger": "Minna", "Ogun": "Abeokuta",
    "Ondo": "Akure", "Osun": "Osogbo", "Oyo": "Ibadan", "Plateau": "Jos",
    "Rivers": "Port Harcourt", "Sokoto": "Sokoto", "Taraba": "Jalingo",
    "Yobe": "Damaturu", "Zamfara": "Gusau"
}

if st.button("Predict"):
    if district == "" or crop == "" or soil not in defined_soils:
        st.error("Please provide all inputs correctly!")
    else:
        # Get soil features
        N = defined_soils[soil]["N"]
        P = defined_soils[soil]["P"]
        K = defined_soils[soil]["K"]
        ph = defined_soils[soil]["ph"]

        # Fetch live weather
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={district},NG&appid={api_key}&units=metric"
            response = requests.get(url)
            weather = response.json()

            if weather.get("cod") != 200:
                capital = fallback_cities.get(district, district)
                url = f"https://api.openweathermap.org/data/2.5/weather?q={capital},NG&appid={api_key}&units=metric"
                response = requests.get(url)
                weather = response.json()

            temp = weather["main"]["temp"]
            humidity = weather["main"]["humidity"]
        except:
            st.error("Could not fetch weather data. Please try again.")
            st.stop()

        # Simulate rainfall
        rainfall = 150 + hash(crop) % 100

        # Prepare input features
        features = np.array([[N, P, K, temp, humidity, ph, rainfall]])
        predicted_crop = model.predict(features)[0].title()
        crop_title = crop.title()

        # Yield estimation
        yield_data_per_hectare = {
            "Maize": 3.0, "Rice": 2.5, "Cassava": 10.0,
            "Tomato": 5.0, "Cocoa": 1.2, "Yam": 7.0, "Groundnut": 2.8
        }

        base_yield = yield_data_per_hectare.get(predicted_crop, 0)
        if base_yield == 0:
            base_yield = yield_data_per_hectare.get(crop_title, 0)

        acre_conversion_factor = 0.4047
        total_yield = base_yield * area * acre_conversion_factor

        # Crop-soil warning
        soil_crop_warnings = {
            "clay": ["Groundnut"], "sandy": ["Rice"], "loamy": []
        }
        warning = f"⚠️ Warning: {soil.capitalize()} soil is not ideal for {crop_title}." \
            if crop_title in soil_crop_warnings.get(soil, []) else ""

        # Display results
        st.success(f"🌾 Predicted Crop: {predicted_crop}")
        st.info(f"Estimated Yield: {round(total_yield,2)} tons")
        if warning:
            st.warning(warning)
