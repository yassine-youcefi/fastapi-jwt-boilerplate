from pydantic import BaseSettings

class Settings(BaseSettings):
    mongo_uri: str = "mongodb://mongo:27017"  # Change this to your MongoDB URI
    jwt_secret: str = "3456789olkjnbvcdswertuybn@y78900-987ytug"  # For JWT
    jwt_algorithm: str = "HS256"
    jwt_expiration_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()