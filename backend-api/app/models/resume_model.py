from typing import List, Optional
from beanie import Document
from pydantic import BaseModel, Field

# Submodels
class PersonalInformation(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    portfolio: Optional[str] = None
    website: Optional[str] = None

class Education(BaseModel):
    degree: Optional[str] = None
    institution: Optional[str] = None
    location: Optional[str] = None
    duration: Optional[str] = None
    cgpa: Optional[str] = None
    percentage: Optional[str] = None

class Project(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    technologies_used: Optional[List[str]] = None
    features: Optional[List[str]] = None
    github_link: Optional[str] = None
    live_demo_link: Optional[str] = None

class Certification(BaseModel):
    certificate_name: Optional[str] = None
    issuer: Optional[str] = None
    platform: Optional[str] = None
    issue_date: Optional[str] = None
    validity: Optional[str] = None

class Experience(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    duration: Optional[str] = None
    responsibilities: Optional[List[str]] = None

# Main Document Model
class Resume(Document):
    user: str = Field(..., description="User ID or reference")
    personal_information: Optional[PersonalInformation] = None
    objective: Optional[str] = None
    education: Optional[List[Education]] = None
    technical_skills: Optional[dict] = None
    projects: Optional[List[Project]] = None
    certifications: Optional[List[Certification]] = None
    languages: Optional[List[str]] = None
    experience: Optional[List[Experience]] = None
    achievements: Optional[List[str]] = None
    extracurricular_activities: Optional[List[str]] = None
    resume: Optional[str] = None
    linkedin_resume: Optional[str] = None

    class Settings:
        name = "resumes"  # MongoDB collection name
