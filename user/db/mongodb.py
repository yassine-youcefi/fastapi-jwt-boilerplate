from pymongo import MongoClient
from core.config import settings

client = MongoClient(settings.mongo_uri)

def get_db():
    return client["boilerplate"]
