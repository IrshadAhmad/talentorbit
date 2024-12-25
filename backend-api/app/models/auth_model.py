from beanie import Document
from pydantic import EmailStr, BaseModel

class LoginModel(Document):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True