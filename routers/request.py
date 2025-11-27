import os
from pandas import DataFrame
from joblib import load
from fastapi import APIRouter, HTTPException
from pydantic import ValidationError
from models.request_models import DataPredict  
import boto3
from io import BytesIO

model_path = os.path.join(os.path.dirname(__file__), '..', 'pipeline.joblib')
model = load(model_path)
s3 = boto3.client('s3')
S3_BUCKET_NAME = 'slr-0923-mlops'

router = APIRouter()

@router.post("/predict")
def predict(request: DataPredict):
    try:
        list_data = request.data_to_predict
        df_data = DataFrame(list_data, columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach','exang', 'oldpeak', 'slope', 'ca', 'thal'])

        prediction = model.predict(df_data)

        prediction_str = "\n".join(map(str, prediction.tolist()))
        prediction_bytes = prediction_str.encode('utf-8')
        file_like_object = BytesIO(prediction_bytes)

        s3_key = 'predictions/prediction1.txt'

        s3.upload_fileobj(file_like_object, S3_BUCKET_NAME, s3_key)

        return {"prediction": prediction.tolist(), "message": "Se guardo en S3!"}
    except ValidationError as ve:
        raise HTTPException(status_code=400, detail=ve.errors())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
def home():
    return {'predictor del corazonnnn': 've a docs de swagger para una prediccion'}