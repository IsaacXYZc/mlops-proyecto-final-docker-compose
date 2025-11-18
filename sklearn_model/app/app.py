from mlflow_utils import get_model, configure_mlflow
from pydantic import BaseModel
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pipeline_runner import run_pipeline
from datetime import datetime
import pandas as pd
import dotenv
import os

dotenv.load_dotenv()

tracking_uri = os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000")
mlfow_experiment = os.getenv("MLFLOW_EXPERIMENT_NAME", "sklearn_model_experiment")
model_name = os.getenv("MLFLOW_MODEL_NAME", "salary_model")

class PredictRequest(BaseModel):
    Store: int
    Date: str  # formato dd-mm-YYYY
    Holiday_Flag: int
    Temperature: float
    Fuel_Price: float
    CPI: float
    Unemployment: float
    
model_cache = None

def get_cached_model():
    '''
    Devuelve el modelo en caché si ya se ha cargado.
    Si no está en caché, intenta cargarlo desde MLflow.
    Returns:
        model: Modelo cargado o None si no se pudo cargar.
    '''
    global model_cache
    if model_cache is None:
        model_cache = get_model(model_name)
        if model_cache is None:
            run_pipeline(model_name)
            model_cache = get_model(model_name)
    return model_cache


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        configure_mlflow(tracking_uri, mlfow_experiment)
    except Exception as e:
        print(f"Error al configurar MLflow: {e}", flush=True)
    yield

app = FastAPI(title="Sklearn model prediction", version="1.0.0", lifespan=lifespan)
    
@app.get("/")
def read_root():
    return {"Hello": "World sklearn model with FastAPI"}

@app.get("/reload_model/")
def reload_model():
    '''
    Fuerza la recarga del modelo desde MLflow.
    Útil si se ha actualizado el modelo y se quiere cargar la nueva versión.
    '''
    global model_cache
    model_cache = get_model()
    if model_cache is None:
        run_pipeline(model_name)
        model_cache = get_model()
    return {"detail": "Modelo recargado exitosamente."}

@app.get("/test_prediction/")
def get_prediction():
    '''
    Realiza una predicción de prueba con datos fijos.
    Para verificar que el modelo está funcionando correctamente.
    '''
    model = get_cached_model()
    if model is None:
        raise HTTPException(status_code=400, detail="Modelo no disponible")
    try:
        data = pd.DataFrame([{
            "Store": 1,
            "Date": "05-02-2010",
            "Holiday_Flag": 0,
            "Temperature": 42.31,
            "Fuel_Price": 2.572,
            "CPI": 211.0963582,
            "Unemployment": 8.106
        }])
        
        prediction = model.predict(data)
        return {"prediction": float(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error indesperado en la predicción: {e}")
    
@app.get("/get_model_info/")
def get_model_info():
    '''
    Devuelve información sobre el modelo cargado.
    Útil para verificar qué modelo está en uso.
    '''
    model = get_cached_model()
    return {"model_info": str(model)}

@app.post("/predict/")
def predict(request: PredictRequest):
    '''
    Realiza una predicción con los datos proporcionados en la solicitud.
    Espera un JSON con los campos necesarios para la predicción.
    Devuelve la predicción como JSON.
    '''
    
    model = get_cached_model()
    if model is None:
        raise HTTPException(status_code=400, detail="Modelo no disponible")
    try:
        data = pd.DataFrame([request.dict()])
        prediction = model.predict(data)
        return {"prediction": float(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error indesperado en la predicción: {e}")
