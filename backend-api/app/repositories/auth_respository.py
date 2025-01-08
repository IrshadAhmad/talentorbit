from app.models.user_model import User

async def find_user_by_email(email: str):
    return await User.find_one(User.email == email)

async def register_user(self, user: User) -> User:
        await user.create()
        return user