# app.py

from flask import Flask, request, jsonify
import pickle
import numpy as np

# 🔹 Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        features = [
            data['N'],
            data['P'],
            data['K'],
            data['temp'],
            data['humidity'],
            data['ph'],
            data['rainfall']
        ]

        prediction = model.predict([np.array(features)])
        return jsonify({"predicted_crop": prediction[0]})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=False)
