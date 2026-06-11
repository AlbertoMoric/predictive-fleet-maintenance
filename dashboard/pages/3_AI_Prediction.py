import streamlit as st
import pandas as pd
import pickle
# cargar modelo (solo una vez)

with open("dashboard/models/best_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🤖 AI Vehicle Failure Prediction")

st.markdown("Introduce los datos del vehículo para predecir el riesgo de fallo.")

# -----------------------------
# INPUTS
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    vehicle_age = st.slider("Vehicle Age (years)", 0, 20, 5)
    km_driven = st.number_input("KM Driven", 0, 500000, 100000)
    engine_temp = st.slider("Engine Temperature", 60, 120, 90)
    vibration_level = st.slider("Vibration Level", 0.0, 1.0, 0.3)

with col2:
    battery_health = st.slider("Battery Health", 0.0, 1.0, 0.8)
    last_service_km = st.number_input("Last Service KM", 0, 500000, 5000)
    maintenance_delay_days = st.number_input("Maintenance Delay (days)", 0, 365, 10)
    driving_hours_day = st.slider("Driving Hours/Day", 0, 24, 6)

load_weight = st.number_input("Load Weight (kg)", 0, 20000, 3000)

# -----------------------------
# PREDICTION BUTTON
# -----------------------------
if st.button("🔍 Analyze Risk"):

    input_data = pd.DataFrame([{
        "vehicle_age": vehicle_age,
        "km_driven": km_driven,
        "engine_temp": engine_temp,
        "vibration_level": vibration_level,
        "battery_health": battery_health,
        "last_service_km": last_service_km,
        "maintenance_delay_days": maintenance_delay_days,
        "driving_hours_day": driving_hours_day,
        "load_weight": load_weight
    }])

    prediction = model.predict(input_data)[0]

    # -----------------------------
    # OUTPUT
    # -----------------------------
    if prediction == 1:
        st.error("🔴 HIGH RISK: Vehicle likely to fail soon")
    else:
        st.success("🟢 LOW RISK: Vehicle is in good condition")

    st.write("Prediction value:", prediction)
