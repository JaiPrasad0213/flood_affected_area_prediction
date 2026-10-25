import joblib
import json
import os

def load_trained_model():
    model_path = os.path.join("models", "weather_random_forest_model.joblib")
    if os.path.exists(model_path):
        return joblib.load(model_path)
    return None

def load_model_metadata():
    meta_path = os.path.join("models", "weather_random_forest_metadata.json")
    if os.path.exists(meta_path):
        with open(meta_path, "r") as f:
            return json.load(f)
    return {}