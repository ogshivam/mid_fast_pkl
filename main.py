# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from predictor import predict

appmodel = FastAPI()

# Define a data model for input
class PredictionInput(BaseModel):
    input_data: list[float]  # Accepts a list of floats

@appmodel.post("/predict")
def get_prediction(data: PredictionInput):
    try:
        # Use the predictor module to generate predictions
        output = predict(data.input_data)
        return {"input": data.input_data, "predictions": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
