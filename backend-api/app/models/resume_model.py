from beanie import Document
from pydantic import BaseModel
from typing import List, Optional
from bson import ObjectId

class Resume(Document):
    name: str
    contact: Optional[str]
    summary: List[str]
    education: List[str]
    certifications: List[str]
    skills: List[str]
    work_experiences: List[str]
    projects: List[str]
    achievements: List[str]
    internships: List[str]
    volunteer_works: List[str]
    languages: List[str]
    hobbies_and_interests: List[str]

    class Settings:
        use_revision = False

    class Config:
        json_encoders = {ObjectId: str}