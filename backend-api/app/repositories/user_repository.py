from typing import List, Optional
from app.models.user_model import User

class UserRepository:
    async def create_user(self, user: User) -> User:
        await user.create()
        return user

    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        return await User.get(user_id)

    async def get_user_by_email(self, email: str) -> Optional[User]:
        return await User.find_one(User.email == email)

    async def list_users(self) -> List[User]:
        return await User.all().to_list()

    async def update_user(self, user_id: str, data: dict) -> Optional[User]:
        user = await User.get(user_id)
        if user:
            await user.set(data)
            return user
        return None

    async def delete_user(self, user_id: str) -> bool:
        user = await User.get(user_id)
        if user:
            await user.delete()
            return True
        return False