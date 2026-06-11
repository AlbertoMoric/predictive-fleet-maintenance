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
