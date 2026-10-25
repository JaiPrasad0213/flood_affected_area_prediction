import streamlit as st
import requests

st.title("🌊 Chennai Flood-Affected Area Prediction App")
st.write("Enter neighborhood metrics and forecasted monsoon conditions to evaluate flood risks.")

zone_code = st.slider("Chennai Corporation Zone Code (1-15)", 1, 15, 13)
rainfall_24hrs_mm = st.number_input("24-Hour Cumulative Rainfall (mm)", value=150.0)
waterbody_distance_km = st.number_input("Distance to Nearest Water Body / Canal (km)", value=0.8)
elevation_meters = st.number_input("Ground Elevation (meters above sea level)", value=3.5)
drainage_capacity = st.slider("Local Drainage Efficiency Index (1-10)", 1.0, 10.0, 4.0)

if st.button("Evaluate Flood Risk"):
    payload = {
        "zone_code": zone_code,
        "rainfall_24hrs_mm": rainfall_24hrs_mm,
        "waterbody_distance_km": waterbody_distance_km,
        "elevation_meters": elevation_meters,
        "drainage_capacity": drainage_capacity
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        if response.status_code == 200:
            res_data = response.json()
            if "High" in res_data['flood_risk_prediction']:
                st.error(f"Prediction: **{res_data['flood_risk_prediction']}**")
            else:
                st.success(f"Prediction: **{res_data['flood_risk_prediction']}**")
            st.info(f"Model Confidence: {res_data['risk_probability'] * 100:.2f}%")
        else:
            st.error("Error communicating with the FastAPI prediction backend.")
    except Exception as e:
        st.error(f"Failed to connect to backend server: {e}")