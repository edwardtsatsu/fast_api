import datetime
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.models.user_model import User
from src.repositories.user_repository import UserRepository
from ..schema.schema import UserIn, UserOut
from ..services.user_service import UserService
from src.config.db import get_db


user_router = APIRouter()
user_repository = UserRepository(db=get_db())
user_service = UserService(user_repository)

@user_router.post("/users")
async def create_user(user: UserIn, db: Session = Depends(get_db)):
    to_create = User(
        username=user.username,
        email=user.email,
        password=user.password,
        created_on = datetime.datetime.today()
    )

    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "created_id": "okay"
    }
    # new_user = user_service.create_user(user)
    # if new_user:
    #     return new_user
    # else:
    #     raise HTTPException(status_code=400, detail="User already exists")


@user_router.get("/users", response_model=List[UserOut])
async def read_users(skip: int = 0, limit: int = 100):
    return user_service.get_users(skip, limit)


@user_router.get("/users/{user_id}", response_model=UserOut)
async def read_user(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@user_router.put("/users/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user: UserIn):
    updated_user = user_service.update_user(user_id, user)
    if updated_user:
        return updated_user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@user_router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    deleted_user = user_service.delete_user(user_id)
    if deleted_user:
        return {"message": "User deleted"}
    else:
        raise HTTPException(status_code=404, detail="User not found")

