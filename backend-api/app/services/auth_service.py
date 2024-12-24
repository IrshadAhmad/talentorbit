# services/auth_service.py
from datetime import timedelta
from app.core.security import hash_password, verify_password
from app.core.jwt import create_access_token
from app.repositories.auth_respository import find_user_by_email, create_user

async def authenticate_user(email: str, password: str):
    """
    Validate user credentials by checking the email and password.
    """
    user = await find_user_by_email(email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

async def login_user(email: str, password: str):
    """
    Authenticate a user and generate a JWT token if valid.
    """
    user = await authenticate_user(email, password)
    if not user:
        return None
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=timedelta(minutes=30)
    )
    return {"access_token": access_token, "token_type": "bearer"}

async def register_user(username: str, email: str, password: str):
    """
    Register a new user after hashing the password.
    """
    existing_user = await find_user_by_email(email)
    if existing_user:
        raise ValueError("User with this email already exists")
    hashed_password = hash_password(password)
    return await create_user(username, email, hashed_password)
