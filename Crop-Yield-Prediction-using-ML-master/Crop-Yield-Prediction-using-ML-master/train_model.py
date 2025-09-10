# train_model.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# 🔹 Load your Nigerian dataset
data = pd.read_csv("Final_Data.csv")

# 🔹 Rename column if needed
if "Crop" in data.columns:
    data.rename(columns={"Crop": "label"}, inplace=True)

# 🔹 Confirm label exists
if "label" not in data.columns:
    raise Exception("❌ 'label' column not found!")

# 🔹 Separate input and output
X = data.drop("label", axis=1)
y = data["label"]

# 🔹 Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 🔹 Save as model.pkl
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
