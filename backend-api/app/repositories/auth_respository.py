from app.models.user_model import User

async def find_user_by_email(email: str):
    """
    Fetch a user document from the database using the email.
    """
    return await User.find_one(User.email == email)

async def create_user(username: str, email: str, hashed_password: str):
    """
    Create a new user in the database.
    """
    new_user = User(username=username, email=email, hashed_password=hashed_password)
    await new_user.insert()
    return new_user