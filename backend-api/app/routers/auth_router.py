from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse
from app.services.auth_service import login_user, register_user

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

@auth_router.post("/register", response_model=UserResponse)
async def register(user_data: UserCreate):
    try:
        # Call the register_user function to handle registration logic
        user = await register_user(user_data)
        return UserResponse.from_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Error registering user: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")