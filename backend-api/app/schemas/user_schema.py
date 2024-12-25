from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]

class UserResponse(BaseModel):
    id: str  # Explicitly declare `id` as a string
    username: str
    email: EmailStr
    is_active: bool