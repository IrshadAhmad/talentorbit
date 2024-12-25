from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.user_model import User
from app.models.auth_model import LoginModel
from app.core.config import settings


class Database:
    def __init__(self):
        self.client = None

    async def connect(self):
        """Initialize the database connection."""
        self.client = AsyncIOMotorClient(settings.DATABASE_URL)
        await init_beanie(database=self.client[settings.DATABASE_NAME], document_models=[User, LoginModel])

    async def close(self):
        """Close the database connection."""
        if self.client:
            self.client.close()

# Create a global instance of the Database class
db = Database()

    

