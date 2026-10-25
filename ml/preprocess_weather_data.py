import pandas as pd
import numpy as np
import os


def preprocess_flood_data():
    os.makedirs("data", exist_ok=True)
    np.random.seed(42)
    n_samples = 1500

    # Simulating Chennai regional factors
    data = {
        "zone_code": np.random.randint(1, 15, n_samples),  # 1 to 15 Corporation Zones
        "rainfall_24hrs_mm": np.random.uniform(20, 250, n_samples),  # Heavy monsoon rains (mm)
        "waterbody_distance_km": np.random.uniform(0.1, 5.0, n_samples),  # Proximity to rivers/canals
        "elevation_meters": np.random.uniform(1, 15, n_samples),  # Chennai low-lying topography
        "drainage_capacity": np.random.uniform(1, 10, n_samples)
    }

    df = pd.DataFrame(data)

    # Logic for flood risk: High rainfall + low elevation + close to waterbody + poor drainage = Flood Risk (1)
    flood_condition = (
                              (df["rainfall_24hrs_mm"] > 120) &
                              (df["elevation_meters"] < 5.0) &
                              (df["waterbody_distance_km"] < 1.5)
                      ) | (df["rainfall_24hrs_mm"] > 200)  # Extreme rain floods anywhere

    df["is_flooded"] = flood_condition.astype(int)

    output_path = os.path.join("data", "chennai_flood_data.csv")
    df.to_csv(output_path, index=False)
    print(f"Chennai historical flood dataset saved to {output_path}")


if __name__ == "__main__":
    preprocess_flood_data()