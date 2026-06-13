import streamlit as st
import pandas as pd
import plotly.express as px
# cargar dataset
df = pd.read_csv("dashboard/data/fleet_dataset.csv")

st.title("📊 Vehicle Analytics")
st.markdown("Fleet monitoring and operational analytics dashboard.")
# -----------------------------
# KPI SECTION
# -----------------------------
total_vehicles = len(df)
high_risk = df["failure_risk"].sum()
avg_temp = round(df["engine_temp"].mean(), 1)
avg_battery = round(df["battery_health"].mean(), 2)
col1, col2, col3, col4 = st.columns(4)
col1.metric("🚛 Total Vehicles", total_vehicles)
col2.metric("🔴 High Risk Vehicles", high_risk)
col3.metric("🌡 Avg Engine Temp", avg_temp)
col4.metric("🔋 Avg Battery Health", avg_battery)
# -----------------------------
# CHARTS SECTION
# -----------------------------
st.subheader("📈 Fleet Insights")
# Row 1
col1, col2 = st.columns(2)
with col1:
    risk_chart = px.histogram(
        df,
        x="failure_risk",
        title="Failure Risk Distribution"
    )
    st.plotly_chart(risk_chart, use_container_width=True)
with col2:
    temp_chart = px.histogram(
        df,
        x="engine_temp",
        nbins=30,
        title="Engine Temperature Distribution"
    )
    st.plotly_chart(temp_chart, use_container_width=True)
# Row 2
col3, col4 = st.columns(2)
with col3:
    battery_chart = px.histogram(
        df,
        x="battery_health",
        nbins=30,
        title="Battery Health Distribution"
    )
    st.plotly_chart(battery_chart, use_container_width=True)
with col4:
    scatter_chart = px.scatter(
        df,
        x="km_driven",
        y="engine_temp",
        color="failure_risk",
        title="KM Driven vs Engine Temperature"
    )
    st.plotly_chart(scatter_chart, use_container_width=True)
# -----------------------------
# VEHICLE EXPLORER
# -----------------------------
st.subheader("🚗 Vehicle Explorer")
# selector
selected_vehicle = st.selectbox(
    "Select Vehicle ID",
    df["vehicle_id"]
)
# filtrar vehículo
vehicle_data = df[df["vehicle_id"] == selected_vehicle]
# obtener primera fila
vehicle = vehicle_data.iloc[0]
# métricas
col1, col2, col3 = st.columns(3)
col1.metric("KM Driven", int(vehicle["km_driven"]))
col2.metric("Engine Temp", round(vehicle["engine_temp"], 1))
col3.metric("Battery Health", round(vehicle["battery_health"], 2))
col4, col5, col6 = st.columns(3)
col4.metric("Vehicle Age", int(vehicle["vehicle_age"]))
col5.metric("Maintenance Delay", int(vehicle["maintenance_delay_days"]))
col6.metric("Driving Hours/Day", round(vehicle["driving_hours_day"], 1))
# riesgo
st.markdown("### Vehicle Status")
if vehicle["failure_risk"] == 1:
    st.error("🔴 HIGH FAILURE RISK")
else:
    st.success("🟢 LOW FAILURE RISK")
# tabla completa opcional
with st.expander("See full vehicle data"):
    st.dataframe(vehicle_data)
st.subheader("➕ Add New Vehicle")
new_vehicle_id = st.text_input("Vehicle ID")
new_vehicle_age = st.number_input(
    "Vehicle Age",
    0,
    30,
    5
)
new_km_driven = st.number_input(
    "KM Driven",
    0,
    1000000,
    100000
)
new_engine_temp = st.slider(
    "Engine Temperature",
    60,
    120,
    90
)
new_vibration = st.slider(
    "Vibration Level",
    0.0,
    1.0,
    0.3
)
new_battery = st.slider(
    "Battery Health",
    0.0,
    1.0,
    0.8
)
new_service_km = st.number_input(
    "Last Service KM",
    0,
    1000000,
    5000
)
new_delay = st.number_input(
    "Maintenance Delay",
    0,
    365,
    10
)
new_driving_hours = st.slider(
    "Driving Hours/Day",
    0,
    24,
    6
)
new_load = st.number_input(
    "Load Weight",
    0,
    50000,
    3000
)
new_failure_risk = st.selectbox(
    "Failure Risk",
    [0, 1]
)
