import streamlit as st
import pandas as pd
import pickle
#---------------------------------------------------------
# título
st.title("Predictive Fleet Maintenance")
# cargar dataset
df = pd.read_csv("dashboard/data/fleet_dataset.csv")
# cargar modelo
import pickle
with open("dashboard/models/best_model.pkl", "rb") as f:
    model = pickle.load(f)    
st.success("App loaded correctly")
st.write(type(model))
#---------------------------------------------------------
