import streamlit as st

st.set_page_config(page_title="Fleet AI System", layout="wide")

# -----------------------------
# HERO
# -----------------------------
st.title("🚛 Predictive Fleet Maintenance AI")

st.markdown("""
### Intelligent fleet monitoring and predictive maintenance system

This platform helps you:
- Predict vehicle failures using AI
- Monitor real-time fleet health
- Analyze operational performance
- Reduce maintenance costs and downtime
""")

st.divider()

# -----------------------------
# VALUE SECTION
# -----------------------------
st.subheader("💡 Key Capabilities")

col1, col2 = st.columns(2)

with col1:
    st.write("🔴 Predict vehicle failure risk")
    st.write("📊 Analyze fleet performance")
    st.write("⚠️ Detect maintenance needs early")

with col2:
    st.write("📡 Real-time insights")
    st.write("📉 Reduce operational costs")
    st.write("🚀 Improve fleet efficiency")

st.divider()

# -----------------------------
# NAVIGATION GUIDE
# -----------------------------
st.subheader("🧭 Navigate the Platform")

st.info("Use the sidebar to access different modules:")

st.markdown("""
- 📊 Overview → Fleet summary and KPIs  
- 🚗 Vehicle Analytics → Detailed fleet analysis  
- 🤖 AI Prediction → Individual vehicle risk prediction  
""")
