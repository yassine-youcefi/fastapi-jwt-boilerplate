from fastapi import APIRouter, HTTPException, Depends
from user.models.user_models import User
from user.controllers.user_controllers import UserController

router = APIRouter()
user_controller = UserController()

@router.post("/register", response_model=User)
async def register_user(user: User):
    try:
        created_user = await user_controller.create_user(user)
        if not created_user:
            raise HTTPException(status_code=400, detail="User creation failed")
        return created_user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: str):
    user = await user_controller.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
