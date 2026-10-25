import os
import joblib
import json
from ml.train_flood_models import train_flood_models


def save_trained_artifacts():
    model, metrics = train_flood_models()
    os.makedirs("models", exist_ok=True)

    model_path = os.path.join("models", "chennai_flood_model.joblib")
    joblib.dump(model, model_path)

    meta_path = os.path.join("models", "chennai_flood_metadata.json")
    with open(meta_path, "w") as f:
        json.dump(metrics, f, indent=4)

    print("Chennai Flood model and metadata successfully saved in /models directory!")


if __name__ == "__main__":
    save_trained_artifacts()