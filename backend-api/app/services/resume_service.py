import os
from fastapi import UploadFile
from bson import ObjectId
from app.utils.resume_parser import extract_resume_data
from app.repositories.resume_repository import ResumeRepository

TEMP_UPLOADS_DIR = "temp_uploads"
os.makedirs(TEMP_UPLOADS_DIR, exist_ok=True)

class ResumeService:
    @staticmethod
    async def upload_and_process_resume(file: UploadFile, user_id: str):
        # Ensure the temp_uploads directory exists
        file_path = os.path.join(TEMP_UPLOADS_DIR, file.filename)

        try:
            # Save the file locally
            print(f"Saving file to: {file_path}")
            with open(file_path, "wb") as buffer:
                buffer.write(await file.read())

            # Extract data from the resume
            extracted_data = extract_resume_data(file_path)

            # Add user-related metadata
            extracted_data["user_id"] = user_id

            # Save resume data to the database
            resume = await ResumeRepository.create_resume(extracted_data)
        finally:
            # Clean up the temporary file
            ResumeService.cleanup_temp_file(file_path)

        return resume

    @staticmethod
    def cleanup_temp_file(file_path: str):
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Failed to delete file {file_path}: {e}")
    
    @staticmethod
    async def get_resume_by_id(resume_id: str):
        # Convert string ID to ObjectId before querying the database
        resume = await ResumeService.get(ObjectId(resume_id))
        if resume:
            # Convert ObjectId to string before returning
            resume_dict = resume.dict()
            resume_dict["id"] = str(resume.id)  # Ensure the ID is returned as a string
            return resume_dict
        return None