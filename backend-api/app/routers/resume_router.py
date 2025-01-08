from fastapi import APIRouter, UploadFile, Request
from app.services.resume_service import ResumeService
from typing import Optional
from app.models.resume_model import Resume

resume_router = APIRouter()
resume_service = ResumeService()


@resume_router.post("/")
async def upload_file(file: UploadFile, request: Request):
    form_data = await request.form()
    file_type = form_data.get("file_type")
    # body = await request.json()  # Parse JSON body
    # print("Request Body:", body)
    return await resume_service.resume_upload(file, file_type, request)


@resume_router.get("/")
async def get_resume():
    return await resume_service.get_all_resume()


@resume_router.get("/resume_id/")
async def get_resume_by_id_query(request: Request):
    return await resume_service.get_resume_by_id(request)


@resume_router.get("/resume_id/{resume_id}/")
async def get_resume_by_id_path(request: Request, resume_id: str):
    return await resume_service.get_resume_by_id(request, resume_id)


@resume_router.put("/")
async def update_user_resume(request: Request, payload: Resume):
    return await resume_service.update_resume(request, payload)


@resume_router.delete("/{resume_id}")
async def delete_resume_by_id(resume_id: str):
    return await resume_service.delete_resume(resume_id)


############generate-json-resume#############
@resume_router.post("/generate-json-resume")
async def generate_resume(request: Request):
    return await resume_service.generate_json_resume(request)
