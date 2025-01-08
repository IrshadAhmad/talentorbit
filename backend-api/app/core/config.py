from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_UPLOADS_DIR = os.path.join(BASE_DIR, "../temp_uploads")

class Settings(BaseSettings):
    PROJECT_NAME: str
    DATABASE_URL: str
    DATABASE_NAME: str
    TEMP_UPLOADS_DIR: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    OPENAI_API_KEY: str
    
    class Config:
        env_file = ".env"

settings = Settings()
