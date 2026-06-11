import streamlit as st
import pandas as pd
import pickle

# título
st.title("Predictive Fleet Maintenance")
# cargar dataset
df = pd.read_csv("dashboard/data/fleet_dataset.csv")
