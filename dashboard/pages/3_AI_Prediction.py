import streamlit as st
import pandas as pd
import pickle
from datetime import datetime
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
    probability = model.predict_proba(input_data)[0][1]
    new_prediction = pd.DataFrame([{
        "timestamp": datetime.now(),
        "vehicle_age": vehicle_age,
        "km_driven": km_driven,
        "engine_temp": engine_temp,
        "vibration_level": vibration_level,
        "battery_health": battery_health,
        "last_service_km": last_service_km,
        "maintenance_delay_days": maintenance_delay_days,
        "driving_hours_day": driving_hours_day,
        "load_weight": load_weight,
        "prediction": int(prediction),
        "probability": round(probability, 3)
    }])
    history_path = "dashboard/data/prediction_history.csv"
    history_df = pd.read_csv(history_path)
    history_df = pd.concat(
        [history_df, new_prediction],
        ignore_index=True
    )
    history_df.to_csv(history_path, index=False)
    risk_factors = []
    recommendations = []
    if engine_temp > 100:
        risk_factors.append("🌡 High engine temperature")
        recommendations.append("Inspect engine cooling system")
    if maintenance_delay_days > 30:
        risk_factors.append("🛠 Excessive maintenance delay")
        recommendations.append("Schedule maintenance immediately")
    if battery_health < 0.4:
        risk_factors.append("🔋 Poor battery health")
        recommendations.append("Inspect or replace battery")
    if km_driven > 200000:
        risk_factors.append("🚛 High mileage detected")
        recommendations.append("Perform full mechanical inspection")
    if vibration_level > 0.7:
        risk_factors.append("📳 Excessive vibration level")
        recommendations.append("Inspect suspension and engine mounts")
    # -----------------------------
    # OUTPUT
    # -----------------------------   
    st.metric(
    "Failure Risk Probability",
    f"{probability*100:.1f}%"
    )
    st.progress(float(probability))
    if probability < 0.3:
        st.success("🟢 LOW RISK")

    elif probability < 0.6:
        st.warning("🟡 MEDIUM RISK")

    else:
        st.error("🔴 HIGH RISK")
    st.subheader("🧠 AI Explanation")
    if len(risk_factors) > 0:
        st.write("Main risk factors detected:")
        for factor in risk_factors:
            st.write(factor)
    else:
        st.success("✅ No critical risk factors detected.")
    st.subheader("🛠 Maintenance Recommendations")
    if len(recommendations) > 0:
        for rec in recommendations:
            st.write(f"✅ {rec}")
    else:
        st.success("No maintenance actions required.")
    st.subheader("📜 Prediction History")
    st.dataframe(
        history_df.tail(10)
    )
