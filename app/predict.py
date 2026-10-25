import numpy as np
from app.model_loader import load_trained_model


def make_prediction(data: dict):
    model = load_trained_model()
    if model is None:
        raise ValueError("Model not found. Please train and save the model first.")

    features = np.array([[
        data["zone_code"],
        data["rainfall_24hrs_mm"],
        data["waterbody_distance_km"],
        data["elevation_meters"],
        data["drainage_capacity"]
    ]])

    prediction = model.predict(features)[0]
    probability = float(np.max(model.predict_proba(features))) if hasattr(model, "predict_proba") else 1.0

    result_label = "High Flood Risk (Affected Area)" if prediction == 1 else "Low Risk (Safe Area)"

    return {
        "flood_risk_prediction": result_label,
        "risk_probability": probability,
        "model_used": "Chennai Flood Risk Random Forest Classifier"
    }