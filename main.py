import datetime as dt
from fastapi import FastAPI
from pymongo import MongoClient
from core.config import settings
from user.views import user_views

app = FastAPI()

# Global variable to store the MongoDB client
client = None

@app.on_event("startup")
async def connect_to_db():
    global client
    client = MongoClient(settings.mongo_uri)
    print("Connected to the database")

@app.on_event("shutdown")
async def close_db_connection():
    global client
    if client:
        client.close()
        print("Database connection closed")

@app.get("/")
async def read_root():
    return {
        "Application": "FastAPI Boilerplate",
        "Purpose": "This is a boilerplate project for FastAPI with MongoDB.",
        "Author": "Yassine Youcefi",
    }

app.include_router(user_views.router, prefix="/user")
