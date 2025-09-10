import streamlit as st
import pickle
import numpy as np
import requests

# OpenWeatherMap API key
api_key = "95348aea3125b4e8881f126ab8cb646b"

# Load trained ML model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Soil NPK + pH values
defined_soils = {
    "loamy":  {"N": 90, "P": 40, "K": 40, "ph": 6.5},
    "sandy":  {"N": 60, "P": 30, "K": 35, "ph": 5.8},
    "clay":   {"N": 75, "P": 45, "K": 50, "ph": 6.8}
}

# 🌦️ Nigerian states mapped to capitals for weather fallback
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

# Yield data per hectare
yield_data_per_hectare = {
    "Maize": 3.0,
    "Rice": 2.5,
    "Cassava": 10.0,
    "Tomato": 5.0,
    "Cocoa": 1.2,
    "Yam": 7.0,
    "Groundnut": 2.8
}

# Soil-crop warnings
soil_crop_warnings = {
    "clay": ["Groundnut"],
    "sandy": ["Rice"],
    "loamy": []
}

# 🚀 Streamlit UI
st.title("🌱 Crop Yield Prediction (Nigeria)")

district = st.selectbox("Select your State/District", list(fallback_cities.keys()))
crop = st.selectbox("Select Crop", list(yield_data_per_hectare.keys()))
area = st.number_input("Enter farm size (in hectares)", min_value=0.1, value=1.0)
soil = st.selectbox("Select Soil Type", list(defined_soils.keys()))

if st.button("Predict Yield"):
    # Get soil values
    soil_vals = defined_soils[soil]
    N, P, K, ph = soil_vals["N"], soil_vals["P"], soil_vals["K"], soil_vals["ph"]

    # 🌦️ Fetch live weather
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
        st.error("⚠️ Could not fetch weather data. Try again later.")
        st.stop()

    # Simulate rainfall
    rainfall = 150 + hash(crop) % 100

    # Predict crop with ML model
    features = np.array([[N, P, K, temp, humidity, ph, rainfall]])
    predicted_crop = str(model.predict(features)[0]).title()

    # Yield calculation
    base_yield = yield_data_per_hectare.get(predicted_crop, yield_data_per_hectare.get(crop, 0))
    total_yield = base_yield * area

    st.success(f"🌾 Predicted Crop Yield: {round(total_yield, 2)} tons")

    # Soil warning
    if crop in soil_crop_warnings.get(soil, []):
        st.warning(f"⚠️ {soil.capitalize()} soil is not ideal for {crop}.")
