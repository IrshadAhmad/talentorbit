from fastapi import Request
from fastapi.responses import JSONResponse
from jose import jwt, JWTError
from app.core.config import settings
from starlette.middleware.base import BaseHTTPMiddleware
from typing import List

public_paths: List[str] = [
    "/",
    "/auth/login",
    "/auth/register",
    "/docs",
    "/redoc",
    "/openapi.json",
]

class AuthMiddleware(BaseHTTPMiddleware):
    """
    Middleware to authenticate requests based on JWT tokens, excluding public paths.
    """
    async def dispatch(self, request: Request, call_next):
        path = request.scope["path"]
        
        # Allow public paths without authentication
        if path in public_paths:
            return await call_next(request)
        
        auth_header = request.headers.get("Authorization")
        if auth_header:
            try:
                token = auth_header.split(" ")[1]
                jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            except JWTError:
                return JSONResponse(
                    {"detail": "Invalid or expired token"}, status_code=401
                )
        else:
            return JSONResponse(
                {"detail": "Authorization header missing"}, status_code=401
            )
        
        return await call_next(request)
