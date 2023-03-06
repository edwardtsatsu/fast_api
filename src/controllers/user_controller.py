from fastapi import APIRouter, HTTPException
from typing import List
from models.user_model import UserIn, UserOut
from services.user_service import UserService

router = APIRouter()
user_service = UserService()

@router.post("/users", response_model=UserOut)
async def create_user(user: UserIn):
    new_user = user_service.create_user(user)
    if new_user:
        return new_user
    else:
        raise HTTPException(status_code=400, detail="User already exists")


@router.get("/users", response_model=List[UserOut])
async def read_users(skip: int = 0, limit: int = 100):
    return user_service.get_users(skip, limit)


@router.get("/users/{user_id}", response_model=UserOut)
async def read_user(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@router.put("/users/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user: UserIn):
    updated_user = user_service.update_user(user_id, user)
    if updated_user:
        return updated_user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    deleted_user = user_service.delete_user(user_id)
    if deleted_user:
        return {"message": "User deleted"}
    else:
        raise HTTPException(status_code=404, detail="User not found")

