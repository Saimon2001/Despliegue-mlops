from pydantic import BaseModel, ValidationError

class DataPredict(BaseModel):
    data_to_predict: list[list] = [[23, 'male', 34.4, 0, 'no', 'southwest'], [35, 'female', 40, 1, 'no', 'northwest']]