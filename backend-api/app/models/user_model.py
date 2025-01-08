from datetime import datetime
from beanie import Document
from pydantic import EmailStr, BaseModel, Field
from bson import ObjectId
from typing import Optional

class User(Document):
    username: str
    email: EmailStr
    hashed_password: Optional[str] = None
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "users"

    class Config:
        json_encoders = {
            ObjectId: str,  # Convert ObjectId to string
        }