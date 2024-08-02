from pymongo import MongoClient
from core.config import settings

# Create a MongoDB client
client = MongoClient(settings.mongo_uri)

# Access the specific database
db = client["boilerplate"]  # Replace with your actual database name

# Access the collection
users_collection = db["users"]

def get_user_collection():
    return users_collection