from beanie import Document
from bson import ObjectId
from pydantic import BaseModel
from typing import Optional

class Resume(Document):
    user_id: str
    email: str
    name: str
    contact: Optional[str]
    summary: Optional[str]
    education: Optional[str]
    certifications: Optional[str]
    skills: Optional[str]
    work_experiences: Optional[str]
    projects: Optional[str]
    achievements: Optional[str]
    internships: Optional[str]
    volunteer_works: Optional[str]
    languages: Optional[str]
    hobbies_and_interests: Optional[str]

    class Collection:
        name = "resumes"
        
    class Config:
        json_encoders = {
            ObjectId: str,  # Convert ObjectId to string
        }