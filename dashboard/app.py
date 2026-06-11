import streamlit as st
import pandas as pd
import pickle

# título
st.title("Predictive Fleet Maintenance")
# cargar dataset
df = pd.read_csv("data/fleet_dataset.csv")
# cargar modelo
with open("models/best_model.pkl", "rb") as f:
    model = pickle.load(f)

st.success("System loaded successfully")
st.write(df.head())
