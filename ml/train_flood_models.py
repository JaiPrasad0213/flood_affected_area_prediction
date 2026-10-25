import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def train_flood_models():
    data_path = os.path.join("data", "chennai_flood_data.csv")
    if not os.path.exists(data_path):
        raise FileNotFoundError("Dataset not found. Run preprocess script first.")

    df = pd.read_csv(data_path)
    X = df[["zone_code", "rainfall_24hrs_mm", "waterbody_distance_km", "elevation_meters", "drainage_capacity"]]
    y = df["is_flooded"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, zero_division=0),
        "recall": recall_score(y_test, y_pred, zero_division=0),
        "f1_score": f1_score(y_test, y_pred, zero_division=0)
    }

    metrics_df = pd.DataFrame([metrics])
    metrics_df.to_csv("weather_model_metrics.csv", index=False)
    print("Chennai Flood model training completed successfully.")

    return model, metrics


if __name__ == "__main__":
    train_flood_models()