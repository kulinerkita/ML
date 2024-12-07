import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from flask import Flask, jsonify, request

app = Flask(__name__)

# Load model
model = load_model("model_ml.keras")

# Load dataset
df_all = pd.read_excel('df_all_new.xlsx')

# Fungsi untuk menghitung jarak Haversine
def calculate_haversine(lat1, lon1, lat2, lon2):
    earth_radius = 6371
    delta_lat = np.radians(lat2 - lat1)
    delta_lon = np.radians(lon2 - lon1)
    a = np.sin(delta_lat / 2)**2 + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(delta_lon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return earth_radius * c

@app.route("/predict", methods=["POST"])
def predict(): 
    try:
        # Mendapatkan data latitude dan longitude dari request JSON
        data = request.get_json()
        if not data or 'latitude' not in data or 'longitude' not in data:
            return jsonify({"error": "Missing latitude or longitude in request"}), 400

        current_lat = data['latitude']
        current_lon = data['longitude']

        # Hitung jarak menggunakan Haversine
        df_all["computed_distance"] = df_all.apply(
            lambda row: calculate_haversine(current_lat, current_lon, row['Latitude'], row['Longitude']), axis=1
        )

        # Hitung weighted rating
        C = df_all['Rating'].mean()
        M = df_all['Reviews'].quantile(0.5)
        df_all['weighted_rating'] = ((df_all['Reviews'] / (df_all['Reviews'] + M)) * df_all['Rating']) + ((M / (df_all['Reviews'] + M)) * C)

        # Ambil fitur untuk prediksi
        features = df_all[['computed_distance', 'weighted_rating']]

        # Normalisasi data fitur
        scaler = MinMaxScaler()
        features_normalized = scaler.fit_transform(features)

        # Prediksi menggunakan model
        df_all["predicted_distance"] = model.predict(features_normalized)

        # Sort hasil berdasarkan predicted_distance
        result = df_all.sort_values(by="predicted_distance", ascending=True)
        top_recommendation = result[["Shop_name", "Rating", "Reviews"]][:10].to_dict(orient="records")

        return jsonify({"success": "Prediksi berhasil", "data": top_recommendation}), 200
    except Exception as error:
        return jsonify({"error": f"{error}"}), 400

if __name__ == "__main__":
    app.run(debug=True)
