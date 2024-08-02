from pymongo import MongoClient
from core.config import settings
from pymongo.collection import Collection


# Create a MongoDB client
client = MongoClient(settings.mongo_uri)

db = client["boilerplate"]

users_collection: Collection = db["users"]
