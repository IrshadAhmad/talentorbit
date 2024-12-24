# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     DATABASE_URL: str = "mongodb+srv://irshadahmad:786$Germany@fladdra.tesai.mongodb.net/TalentOrbitDB"
#     PROJECT_NAME: str = "Talent Orbit App"

# settings = Settings()

from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
class Settings(BaseSettings):
    DATABASE_URL: str = MONGODB_URI
    DATABASE_NAME: str = MONGO_DB_NAME
    PROJECT_NAME: str = MONGO_DB_NAME

settings = Settings()
