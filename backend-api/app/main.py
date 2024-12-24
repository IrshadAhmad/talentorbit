import os
from fastapi import FastAPI
from werkzeug.utils import secure_filename
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.core.database import db
from app.core.config import settings
from app.routers.user_router import router as user_router
from app.routers.auth_router import auth_router
from app.routers import resume_router
from app.core.config import TEMP_UPLOADS_DIR


app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
async def startup_event():
    await db.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await db.close()

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(resume_router.router, prefix="/resume", tags=["resumes"])

os.makedirs(TEMP_UPLOADS_DIR, exist_ok=True)

@app.get("/")
async def read_root():
    return {"message": "Welcome to my FastAPI application!"}