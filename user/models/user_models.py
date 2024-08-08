from typing import Optional
from pydantic import BaseModel, Field, validator
from bson import ObjectId


class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    username: str
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    hashed_password: Optional[str] = None
    
    class Config:
        allow_population_by_field_name = True
    
    @validator("id", pre=True, always=True)
    def convert_objectid(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value
    

class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    hashed_password: Optional[str]

    class Config:
        allow_population_by_field_name = True
