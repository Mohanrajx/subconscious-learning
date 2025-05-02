import streamlit as st
import joblib
import numpy as np

st.title("🧠 Subconscious Learning Sleep Stage Predictor")

# Load model
model = joblib.load("model/sleep_stage_model.h5")

# Input box
x = st.text_input("📥 Enter 4 comma-separated EEG-like values")

if st.button("🎯 Predict Sleep Stage"):
    try:
        features = np.array([float(i) for i in x.split(",")]).reshape(1, -1)
        prediction = model.predict(features)
        st.success(f"✅ Predicted Sleep Stage: {prediction[0]}")
    except:
        st.error("❌ Please enter exactly 4 numeric values separated by commas.")
