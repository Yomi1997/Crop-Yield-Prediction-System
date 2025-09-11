# RF_predict.py 

import sys
import pickle
import numpy as np
import requests

# OpenWeatherMap API key
api_key = "95348aea3125b4e8881f126ab8cb646b"

# Get command-line input
if len(sys.argv) < 5:
    print("0|")
    sys.exit()

district = sys.argv[1]  # State or LGA
crop = sys.argv[2]
area = float(sys.argv[3])
soil = sys.argv[4].lower()

# Soil NPK + pH values
defined_soils = {
    "loamy":  {"N": 90, "P": 40, "K": 40, "ph": 6.5},
    "sandy":  {"N": 60, "P": 30, "K": 35, "ph": 5.8},
    "clay":   {"N": 75, "P": 45, "K": 50, "ph": 6.8}
}

if soil not in defined_soils:
    print("0|")
    sys.exit()

N = defined_soils[soil]["N"]
P = defined_soils[soil]["P"]
K = defined_soils[soil]["K"]
ph = defined_soils[soil]["ph"]

# 🌦️ Nigerian states mapped to capitals for weather fallback
fallback_cities = {
    "Abia": "Umuahia",
    "Adamawa": "Yola",
    "Akwa Ibom": "Uyo",
    "Anambra": "Awka",
    "Bauchi": "Bauchi",
    "Bayelsa": "Yenagoa",
    "Benue": "Makurdi",
    "Borno": "Maiduguri",
    "Cross River": "Calabar",
    "Delta": "Asaba",
    "Ebonyi": "Abakaliki",
    "Edo": "Benin City",
    "Ekiti": "Ado-Ekiti",
    "Enugu": "Enugu",
    "FCT": "Abuja",
    "Gombe": "Gombe",
    "Imo": "Owerri",
    "Jigawa": "Dutse",
    "Kaduna": "Kaduna",
    "Kano": "Kano",
    "Katsina": "Katsina",
    "Kebbi": "Birnin Kebbi",
    "Kogi": "Lokoja",
    "Kwara": "Ilorin",
    "Lagos": "Ikeja",
    "Nasarawa": "Lafia",
    "Niger": "Minna",
    "Ogun": "Abeokuta",
    "Ondo": "Akure",
    "Osun": "Osogbo",
    "Oyo": "Ibadan",
    "Plateau": "Jos",
    "Rivers": "Port Harcourt",
    "Sokoto": "Sokoto",
    "Taraba": "Jalingo",
    "Yobe": "Damaturu",
    "Zamfara": "Gusau"
}

# 🌦️ Fetch live weather data (with fallback to capital city)
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
    print("0|")
    sys.exit()

# Simulate rainfall
rainfall = 150 + hash(crop) % 100

# Load trained ML model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Prepare input features
features = np.array([[N, P, K, temp, humidity, ph, rainfall]])
predicted_crop = model.predict(features)[0]

# ✅ Normalize crop names to Title case for dictionary matching
predicted_crop = str(predicted_crop).title()
crop = str(crop).title()

# Estimate yield by crop (per hectare), multiply by 0.4047 for acres
yield_data_per_hectare = {
    "Maize": 3.0,
    "Rice": 2.5,
    "Cassava": 10.0,
    "Tomato": 5.0,
    "Cocoa": 1.2,
    "Yam": 7.0,
    "Groundnut": 2.8
}

# First try ML-predicted crop
base_yield = yield_data_per_hectare.get(predicted_crop, 0)

# If model prediction not in dictionary, fall back to user's selected crop
if base_yield == 0:
    base_yield = yield_data_per_hectare.get(crop, 0)

acre_conversion_factor = 0.4047
total_yield = base_yield * area * acre_conversion_factor

# Add crop-soil warning logic
soil_crop_warnings = {
    "clay": ["Groundnut"],
    "sandy": ["Rice"],
    "loamy": []
}

if crop in soil_crop_warnings.get(soil, []):
    warning = f"Warning: {soil.capitalize()} soil is not ideal for {crop}."
else:
    warning = ""

# Output both yield and warning
print(f"{round(total_yield, 2)}|{warning}")
