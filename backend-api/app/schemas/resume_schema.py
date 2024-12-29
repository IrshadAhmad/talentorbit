from pydantic import BaseModel
from typing import List, Optional

class ResumeResponse(BaseModel):
    id: str
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
    user_id: str
    email: str