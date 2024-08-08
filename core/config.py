from pydantic import BaseSettings
from os import environ

class Settings(BaseSettings):
    mongo_uri: str = environ.get("MONGO_URI", "mongodb://mongo:27017")
    database_name: str = environ.get("DATABASE_NAME", "boilerplate")
    jwt_secret: str = "3456789olkjnbvcdswertuybn@y78900-987ytug"
    jwt_algorithm: str = "HS256"
    jwt_expiration_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()