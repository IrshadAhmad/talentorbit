from beanie import PydanticObjectId
from pydantic import BaseModel
from typing import List, Optional

class ResumeResponse(BaseModel):
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

    class Config:
        json_schema_extra  = {
            "example": {
                "id": "646affadc2c941930c41e9e9",
                "name": "John Doe",
                "contact": "+123456789",
                "summary": ["Experienced software developer..."],
                "education": ["BSc in Computer Science"],
                "certifications": ["AWS Certified Developer"],
                "skills": ["Python", "FastAPI"],
                "work_experiences": ["Software Engineer at XYZ"],
                "projects": ["Project A", "Project B"],
                "achievements": ["Best Developer Award"],
                "internships": ["Internship at ABC"],
                "volunteer_works": ["Volunteering at Non-Profit"],
                "languages": ["English", "Spanish"],
                "hobbies_and_interests": ["Hiking", "Photography"]
            }
        }