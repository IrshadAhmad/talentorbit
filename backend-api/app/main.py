import os
from fastapi import FastAPI
from werkzeug.utils import secure_filename
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.core.database import db
from app.core.config import settings
from app.routers.user_router import user_router
from app.routers.auth_router import auth_router
from app.routers.resume_router import resume_router
from app.middlewares.cors_middleware import add_cors_middleware
from app.middlewares.auth_middleware import AuthMiddleware

app = FastAPI(title=settings.PROJECT_NAME)

add_cors_middleware(app)

@app.on_event("startup")
async def startup_event():
    await db.connect()
    print("Connected to MongoDB: "+settings.DATABASE_NAME)

@app.on_event("shutdown")
async def shutdown_event():
    await db.close()

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(resume_router, prefix="/resumes", tags=["resumes"])

os.makedirs(settings.TEMP_UPLOADS_DIR, exist_ok=True)

@app.get("/")
async def read_root():
    return {"message": "Welcome to my FastAPI application!"}