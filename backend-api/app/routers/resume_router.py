from fastapi import APIRouter, UploadFile, Depends, HTTPException
from app.services.resume_service import ResumeService
from app.repositories.resume_repository import ResumeRepository
from app.schemas.resume_schema import ResumeResponse
from typing import List

router = APIRouter()

@router.post("/upload", response_model=ResumeResponse)
async def upload_resume(file: UploadFile, user_id: str):
    """
    Upload and process a resume.
    """
    if file.content_type not in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF and DOCX are allowed.")
    
    resume = await ResumeService.upload_and_process_resume(file, user_id)
    return ResumeResponse(**resume.dict())

@router.get("/{resume_id}", response_model=ResumeResponse)
async def get_resume(resume_id: str):
    """
    Fetch a resume by its ID.
    """
    resume = await ResumeRepository.get_resume_by_id(resume_id)
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found.")
    return ResumeResponse(**resume.dict())

@router.get("/", response_model=List[ResumeResponse])
async def get_all_resumes():
    """
    Fetch all resumes.
    """
    resumes = await ResumeRepository.get_all_resumes()
    return [ResumeResponse(**resume.dict()) for resume in resumes]

@router.delete("/{resume_id}")
async def delete_resume(resume_id: str):
    """
    Delete a resume by its ID.
    """
    success = await ResumeRepository.delete_resume(resume_id)
    if not success:
        raise HTTPException(status_code=404, detail="Resume not found.")
    return {"detail": "Resume deleted successfully"}