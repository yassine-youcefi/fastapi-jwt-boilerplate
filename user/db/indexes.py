from pymongo import MongoClient
from core.config import settings

client = MongoClient(settings.mongo_uri)
db = client["boilerplate"]
users_collection = db["users"]

# Create unique indexes
users_collection.create_index("username", unique=True)
users_collection.create_index("email", unique=True)

print("Unique indexes created on username and email.")