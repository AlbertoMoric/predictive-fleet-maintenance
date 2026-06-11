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
