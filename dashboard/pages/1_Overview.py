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

st.subheader("🚨 Fleet Alerts")
high_risk_count = len(
    df[df["failure_risk"] == 1]
)
high_temp_count = len(
    df[df["engine_temp"] > 100]
)
low_battery_count = len(
    df[df["battery_health"] < 0.4]
)
maintenance_delay_count = len(
    df[df["maintenance_delay_days"] > 30]
)
if high_risk_count > 0:
    st.error(
        f"🔴 {high_risk_count} vehicles with high failure risk"
    )
if high_temp_count > 0:
    st.warning(
        f"🟠 {high_temp_count} vehicles with critical engine temperature"
    )
if low_battery_count > 0:
    st.warning(
        f"🟡 {low_battery_count} vehicles with low battery health"
    )
if maintenance_delay_count > 0:
    st.info(
        f"🔧 {maintenance_delay_count} vehicles overdue maintenance"
    )
if (
    high_risk_count == 0
    and high_temp_count == 0
    and low_battery_count == 0
    and maintenance_delay_count == 0
):
    st.success("✅ No active fleet alerts")
# -----------------------------
# STATUS SECTION
# -----------------------------
risk_ratio = df["failure_risk"].mean()
if risk_ratio < 0.2:
    status = "🟢 Fleet Status: Stable"
    message = "All systems operating normally."
elif risk_ratio < 0.5:
    status = "🟡 Fleet Status: Warning"
    message = "Some vehicles require attention."
else:
    status = "🔴 Fleet Status: Critical"
    message = "Immediate maintenance required for multiple vehicles."
st.subheader("🚦 Fleet Status")
st.markdown(f"### {status}")
st.write(message)
# -----------------------------
# ALERTS SECTION
# -----------------------------
alerts_df = df[df["failure_risk"] == 1]
alerts_df = alerts_df[[
    "vehicle_id",
    "km_driven",
    "engine_temp",
    "battery_health",
    "maintenance_delay_days"
]]
st.subheader("🚨 Active Alerts")
if len(alerts_df) == 0:
    st.success("🟢 No active alerts. Fleet is healthy.")
else:
    st.warning(f"⚠️ {len(alerts_df)} vehicles require attention")
    st.dataframe(alerts_df)
