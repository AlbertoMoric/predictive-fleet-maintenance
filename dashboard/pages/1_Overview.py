import streamlit as st
import pandas as pd
# dataset
df = pd.read_csv("dashboard/data/fleet_dataset.csv")
# -----------------------------
# HERO SECTION
# -----------------------------
st.title("🚛 Predictive Fleet Maintenance")
st.markdown("""
Welcome to the fleet monitoring dashboard.
Monitor vehicle health, detect potential failures,
and analyze fleet performance in real time.
""")
# -----------------------------
# KPIs SECTION
# -----------------------------
st.subheader("📊 Fleet Overview KPIs")
fleet_size = len(df)
active_alerts = df["failure_risk"].sum()
avg_battery = round(df["battery_health"].mean(), 2)
avg_temp = round(df["engine_temp"].mean(), 1)
col1, col2, col3, col4 = st.columns(4)
col1.metric("🚛 Fleet Size", fleet_size)
col2.metric("⚠️ Active Alerts", active_alerts)
col3.metric("🔋 Avg Battery Health", avg_battery)
col4.metric("🌡 Avg Engine Temp", avg_temp)
# -----------------------------
# STATUS SECTION
# -----------------------------
st.subheader("🚦 Fleet Status")
st.markdown(f"### {status}")
st.write(message)
