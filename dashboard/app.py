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
input_data = [[
    5,      # vehicle_age
    120000, # km_driven
    90,     # engine_temp
    0.3,    # vibration_level
    0.8,    # battery_health
    5000,   # last_service_km
    10,     # maintenance_delay_days
    6,      # driving_hours_day
    3000    # load_weight
]]

prediction = model.predict(input_data)

st.write("Failure risk:", prediction[0])
