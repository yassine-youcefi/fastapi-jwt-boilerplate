from pymongo.errors import DuplicateKeyError
from user.models.user_models import User
from user.db.mongodb import users_collection
from bson.objectid import ObjectId
from typing import Optional


class UserController:
    async def create_user(self, user_data: User) -> Optional[User]:
        user_dict = user_data.dict(exclude={"id"})
        
        try:
            # Insert the user data into the collection
            result = users_collection.insert_one(user_dict)
            
            # Fetch the inserted document using the correct ObjectId query
            created_user = users_collection.find_one({"_id": result.inserted_id})
            
            if created_user is None:
                raise ValueError("User was not created successfully.")
            
            # Convert ObjectId to string
            created_user["_id"] = str(created_user["_id"])
            
            # Return a Pydantic model that will serialize the data properly
            return User(**created_user)
        except DuplicateKeyError:
            raise ValueError("Username or email already exists.")

    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        user_data = users_collection.find_one({"_id": ObjectId(user_id)})
        if user_data:
            return User(**user_data)
        return None

    async def get_user_by_username(self, username: str) -> Optional[User]:
        user_data = users_collection.find_one({"username": username})
        if user_data:
            return User(**user_data)
        return None

    async def update_user(self, user_id: str, update_data: dict) -> bool:
        result = users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
        return result.modified_count > 0

    async def delete_user(self, user_id: str) -> bool:
        result = users_collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0
