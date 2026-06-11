import streamlit as st
import pandas as pd
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
