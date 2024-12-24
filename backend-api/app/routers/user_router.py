from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.user_schema import UserCreate, UserUpdate, UserResponse
from app.services.user_service import UserService
from app.models.user_model import User

router = APIRouter()
user_service = UserService()

def serialize_user(user: User) -> dict:
    return {
        "id": str(user.id),
        "username": user.username,
        "email": user.email,
        "is_active": user.is_active,
    }

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
    created_user = await user_service.create_user(user)
    return serialize_user(created_user)

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    user = await user_service.get_user_by_id(user_id)
    if not user.hashed_password:
        raise HTTPException(status_code=404, detail="User not found")
    return serialize_user(user)

@router.get("/", response_model=List[UserResponse])
async def list_users():
    users = await user_service.list_users()
    return [serialize_user(user) for user in users]

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user: UserUpdate):
    updated_user = await user_service.update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return serialize_user(updated_user)

@router.delete("/{user_id}", response_model=bool)
async def delete_user(user_id: str):
    deleted = await user_service.delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted