from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user_schema import UserCreate, UserLogin, UserResponse
from app.services.auth_service import AuthService

auth_router = APIRouter()
auth_service = AuthService()

@auth_router.post("/login")
async def login(user_login: UserLogin):
    logged_user = await auth_service.login_user(user_login.email, user_login.password)
    if not logged_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return logged_user

@auth_router.post("/register", response_model=UserResponse)
async def register(user_data: UserCreate):
    try:
        # Call the register_user function to handle registration logic
        user = await auth_service.register_user(user_data)
        return UserResponse.from_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(f"Error registering user: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")