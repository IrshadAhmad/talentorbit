from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_UPLOADS_DIR = os.path.join(BASE_DIR, "../temp_uploads")

class Settings(BaseSettings):
    DATABASE_URL: str = MONGODB_URI
    DATABASE_NAME: str = MONGO_DB_NAME
    PROJECT_NAME: str = MONGO_DB_NAME

settings = Settings()
