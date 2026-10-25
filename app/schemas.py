from pydantic import BaseModel

class FloodInput(BaseModel):
    zone_code: int  # e.g., representing Chennai zones like Velachery, T. Nagar, Adyar, etc.
    rainfall_24hrs_mm: float  # Cumulative rainfall in mm
    waterbody_distance_km: float  # Distance to nearest river/canal (Adyar, Cooum, Buckingham Canal)
    elevation_meters: float  # Ground elevation above sea level
    drainage_capacity: float  # Index of local drainage efficiency (0 to 10)

class PredictionResponse(BaseModel):
    flood_risk_prediction: str
    risk_probability: float
    model_used: str