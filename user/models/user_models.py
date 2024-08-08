from typing import Optional
from pydantic import BaseModel, Field, validator
from bson import ObjectId


class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    username: str
    email: str
    first_name: str
    last_name: str
    phone_number: str
    hashed_password: Optional[str] = None
    
    class Config:
        # Allow population by field alias to ensure the model uses the alias
        allow_population_by_field_name = True
    
    @validator("id", pre=True, always=True)
    def convert_objectid(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value
