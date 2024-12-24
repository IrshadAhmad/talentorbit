from typing import List, Optional
from app.repositories.user_repository import UserRepository
from app.models.user_model import User
from app.core.security import hash_password
from app.schemas.user_schema import UserCreate, UserUpdate

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    async def create_user(self, data: UserCreate) -> User:
        hashed_password = hash_password(data.password)
        user = User(username=data.username, email=data.email, hashed_password=hashed_password)
        return await self.repository.create_user(user)

    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        return await self.repository.get_user_by_id(user_id)

    async def list_users(self) -> List[User]:
        return await self.repository.list_users()

    async def update_user(self, user_id: str, data: UserUpdate) -> Optional[User]:
        update_data = data.dict(exclude_unset=True)
        if "password" in update_data:
            update_data["hashed_password"] = hash_password(update_data.pop("password"))
        return await self.repository.update_user(user_id, update_data)

    async def delete_user(self, user_id: str) -> bool:
        return await self.repository.delete_user(user_id)

