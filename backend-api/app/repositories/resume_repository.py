from beanie import PydanticObjectId
from app.models.resume_model import Resume
from typing import Optional

async def save_resume(resume_data: dict) -> Resume:
    """
    Save the resume to the database. If a resume already exists for the user, it replaces it.
    """
    existing_resume = await Resume.find_one(Resume.user_id == resume_data["user_id"])
    if existing_resume:
        await existing_resume.delete()
    resume = Resume(**resume_data)
    await resume.insert()
    return resume

async def get_user_resume(user_id: str) -> Optional[Resume]:
    """
    Retrieve the resume for a given user by their user ID.
    """
    return await Resume.find_one(Resume.user_id == user_id)

async def delete_user_resume(user_id: str) -> None:
    """
    Delete the resume for a given user by their user ID.
    """
    resume = await Resume.find_one(Resume.user_id == user_id)
    if resume:
        await resume.delete()