### API LIBRARIES
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from json import dumps
from uvicorn import run
import os
from pydantic import BaseModel
from starlette.responses import JSONResponse

### MODEL LIBRARIES
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
import joblib
import numpy as np

app = FastAPI()

origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers    
)






pipeline = joblib.load('models/iris_pl_clf.pkl')






@app.get("/")
async def root():
    return {"message":"Welcome to IRIS Classifier - This is a test deployment of an iris dataset classifier model "}


@app.post("/")
async def root(inputs : dict):
    
    predict = pipeline.predict(inputs["X"])

    return {
        "predict": str(predict)
    }

  
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    run(app, host="0.0.0.0", port=port)