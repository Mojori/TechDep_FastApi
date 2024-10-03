from pydantic import BaseModel

class TrainSchema(BaseModel):
    fist_row:str
    second_row:str

class PersonSchema(BaseModel):
    name:str
    surname:str
    age:int

class GetFromName(BaseModel):
    name:str