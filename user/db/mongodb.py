from pymongo import MongoClient
from core.config import settings
from pymongo.collection import Collection


# Create a MongoDB client
client = MongoClient(settings.mongo_uri)

# Access the specific database
db = client["boilerplate"]  # Replace with your actual database name

# Access the collection
users_collection: Collection = db["users"]
