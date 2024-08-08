from pymongo.errors import DuplicateKeyError
from user.models.user_models import User, UserUpdate
from pymongo.collection import Collection
from bson.objectid import ObjectId
from typing import Optional


class UserController:
    async def create_user(self, user_data: User, db: Collection) -> Optional[User]:
        users_collection = db["users"]
        user_dict = user_data.dict(exclude={"id"})

        try:
            # Insert the user data into the collection
            result = users_collection.insert_one(user_dict)

            # Fetch the inserted document using the correct ObjectId query
            created_user = users_collection.find_one(
                {"_id": result.inserted_id})

            if created_user is None:
                raise ValueError("User was not created successfully.")

            return User(**created_user)

        except DuplicateKeyError as e:
            # Check which field caused the error
            if "username" in str(e):
                raise ValueError("Username already exists.")
            elif "email" in str(e):
                raise ValueError("Email already exists.")
            else:
                raise ValueError("Username or email already exists.")

    async def get_user_by_id(self, user_id: str, db: Collection) -> Optional[User]:
        users_collection = db["users"]
        user_data = users_collection.find_one({"_id": ObjectId(user_id)})

        if user_data:
            return User(**user_data)
        return None

    async def update_user(self, user_id: str, user_data: UserUpdate, db: Collection) -> Optional[User]:
        users_collection = db["users"]
        user_dict = user_data.dict(exclude_unset=True)

        try:
            updated_user = users_collection.find_one_and_update(
                {"_id": ObjectId(user_id)},
                {"$set": user_dict},
                return_document=True
            )

            if updated_user:
                updated_user["_id"] = str(updated_user["_id"])
                return User(**updated_user)
            return None
        except DuplicateKeyError as e:
            # Check which field caused the error
            if "username" in str(e):
                raise ValueError("Username already exists.")
            elif "email" in str(e):
                raise ValueError("Email already exists.")
            else:
                raise ValueError("Username or email already exists.")
