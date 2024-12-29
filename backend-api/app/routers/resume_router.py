from fastapi import APIRouter, UploadFile, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from app.services.resume_service import extract_resume_content
from app.schemas.resume_schema import ResumeResponse
from app.utils.utils import get_current_user

resume_router = APIRouter()

@resume_router.post("/upload_resume", response_model=ResumeResponse)
async def upload_resume(file: UploadFile, current_user: dict = Depends(get_current_user)):
    """
    Upload a resume file and extract its content for display.
    """
    if file.content_type not in [
        "application/pdf",
        "application/msword",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid file type")
    
    extracted_content = await extract_resume_content(file)
    extracted_content.update({"user_id": current_user["user_id"], "email": current_user["email"]})
    return JSONResponse(status_code=status.HTTP_200_OK, content=extracted_content)