from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user_schema import UserLogin
from app.services.auth_service import login_user

auth_router = APIRouter()

@auth_router.post("/login")
async def login(user_login: UserLogin):
    """
    Authenticate a user and return a JWT token.
    """
    token = await login_user(user_login.email, user_login.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return token