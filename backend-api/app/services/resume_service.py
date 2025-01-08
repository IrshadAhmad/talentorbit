from fastapi import HTTPException, UploadFile, Request
from typing import Optional
from app.models.resume_model import Resume
from app.repositories.resume_repository import ResumeRepository
from pydantic import ValidationError


class ResumeService:
    def __init__(self):
        self.resume_repository = ResumeRepository()

    async def resume_upload(self, file: UploadFile, file_type: Optional[str], request: Request):
        """
        Upload and store a resume file using ResumeRepository.
        """
        try:
            return await self.resume_repository.resume_upload(file, file_type, request)
        except HTTPException as exc:
            raise exc
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error uploading resume: {str(e)}")

    async def get_all_resume(self):
        """
        Retrieve all resumes using ResumeRepository.
        """
        try:
            return await self.resume_repository.get_all_resumes()
        except HTTPException as exc:
            raise exc
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching resumes: {str(e)}")

    async def get_resume_by_id(self, request: Request, resume_id: Optional[str] = None):
        """
        Retrieve a resume by ID or user ID using ResumeRepository.
        """
        try:
            return await self.resume_repository.get_resume_by_id(request, resume_id)
        except HTTPException as exc:
            raise exc
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching resume by ID: {str(e)}")

    async def update_resume(self, request: Request, payload: Resume):
        """
        Update a resume using ResumeRepository.
        """
        try:
            return await self.resume_repository.update_resume(request, payload)
        except ValidationError as ve:
            raise HTTPException(status_code=422, detail=ve.errors())
        except HTTPException as exc:
            raise exc
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error updating resume: {str(e)}")

    async def delete_resume(self, resume_id: str):
        """
        Delete a resume by ID using ResumeRepository.
        """
        try:
            return await self.resume_repository.delete_resume(resume_id)
        except HTTPException as exc:
            raise exc
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error deleting resume: {str(e)}")

    async def generate_json_resume(self, request: Request):
        """
        Generate a JSON resume using ResumeRepository.
        """
        try:
            return await self.resume_repository.generate_json_resume(request)
        except HTTPException as exc:
            raise exc
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error generating JSON resume: {str(e)}")
