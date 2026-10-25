from fastapi import FastAPI, HTTPException
from app.schemas import FloodInput, PredictionResponse
from app.predict import make_prediction

app = FastAPI(title="Chennai Flood Prediction API", version="1.0")

@app.get("/")
def home():
    return {"message": "Welcome to the Chennai Flood-Affected Area Prediction API. Use /predict to get forecasts."}

@app.post("/predict", response_model=PredictionResponse)
def predict_flood(input_data: FloodInput):
    try:
        result = make_prediction(input_data.dict())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))