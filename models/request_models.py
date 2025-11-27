from pydantic import BaseModel, ValidationError

class DataPredict(BaseModel):
    data_to_predict: list[list] = [[52,1,0,125,212,0,1,168,0,1,2,2,3],[34,0,1,118,210,0,1,192,0,0.7,2,0,2]]