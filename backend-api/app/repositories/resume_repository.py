import os
from fastapi import UploadFile, HTTPException, Response
from app.utils.resume_parser import (
    extract_text_from_doc,
    extract_text_from_pdf,
    merge_resume_data,
)
from app.utils.langchain_llm import invoke
from app.utils.prompt import resume_get_prompt
from app.core.database import db
from app.models.resume_model import Resume
from app.utils.str_to_json import extract_json_from_string
from bson import ObjectId
from typing import Optional
from pydantic import ValidationError
from app.core.config import settings


TEMP_UPLOADS_DIR = settings.TEMP_UPLOADS_DIR
os.makedirs(TEMP_UPLOADS_DIR, exist_ok=True)

class ResumeRepository:
    # _instance: Optional["ResumeRepository"] = None

    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance

    # def __init__(self):
    #     if not hasattr(self, "_initialized"):
    #         self._initialized = True
            # self.current_db = db.get_database()
            # self.resume_collection = self.current_db["resume"]

    async def resume_upload(self, file: UploadFile, file_type: str, request):
        if file.content_type not in [
            "application/pdf",
            "application/msword",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ]:
            raise HTTPException(
                status_code=400,
                detail="Invalid file type. Only PDF and DOC/DOCX files are allowed.",
            )

        file_location = os.path.join(TEMP_UPLOADS_DIR, file.filename)
        # print("reuest state", request)
        # current_db = db.get_database()
        # resume_collection = current_db["resume"]
        # users_collection = current_db["users"]
        user_id = request.state.user_id
        print("======================", user_id)

        try:
            with open(file_location, "wb") as buffer:
                buffer.write(await file.read())

            if file.content_type == "application/pdf":
                new_file_content = extract_text_from_pdf(file_location)
            elif file.content_type in [
                "application/msword",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            ]:
                new_file_content = extract_text_from_doc(file_location)

            update_field = ""
            resume_data = {"user": user_id}
            if file_type.strip() == "resume":
                resume_data["resume"] = new_file_content
                update_field = "resume"
            elif file_type.strip() == "linkedin":
                resume_data["linkedin_resume"] = new_file_content
                update_field = "linkedin"
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid file_type. Must be 'resume' or 'linkedin'.",
                )
            # print("resume_data",resume_data)
            # await resume_collection.update_one(
            #     {"user": request.state.user_id}, {"$set": resume_data}, upsert=True
            # )

            # await users_collection.update_one(
            #     {"_id": ObjectId(request.state.user_id)}, {"$set": {update_field: True}}
            # )

            # return {
            #     "message": f"{file_type.capitalize()} file uploaded successfully.",
            #     "file_path": file_location,
            # }
        except HTTPException as exc:
            raise exc
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

    async def get_all_resumes():
        current_db = db.get_database()
        resume_collection = current_db["resume"]
        resume_cursor = resume_collection.find()
        all_resume = []
        async for resumes in resume_cursor:
            resumes["id"] = str(resumes.pop("_id"))
            all_resume.append(resumes)
        if not all_resume:
            raise HTTPException(status_code=404, detail="No resumes found")
        return {"count": len(all_resume), "resumes": all_resume}

    # get by user id or resume id
    async def get_resume_by_id(request, resume_id: Optional[str] = None):
        current_db = db.get_database()
        resume_collection = current_db["resume"]

        if resume_id is None:
            user_id = str(request.state.user_id)
            resume = await resume_collection.find_one({"user": user_id})
        else:
            if not ObjectId.is_valid(resume_id):
                raise HTTPException(status_code=400, detail="Invalid resume ID format")
            resume = await resume_collection.find_one({"_id": ObjectId(resume_id)})
        if not resume:
            raise HTTPException(status_code=404, detail="Resume not found")
        resume["_id"] = str(resume["_id"])
        return {"message": "Resume fetched successfully", "resume": resume}

    async def update_resume(request, payload: Resume):
        current_db = db.get_database()
        resume_collection = current_db["resume"]
        user_id = request.state.user_id

        if not ObjectId.is_valid(user_id):
            raise HTTPException(status_code=400, detail="Invalid user ID format")

        existing_resume = await resume_collection.find_one({"user": user_id})
        if not existing_resume:
            raise HTTPException(status_code=404, detail="Resume not found")

        try:
            payload.linkedin_resume = existing_resume.get("linkedin_resume", "")
            payload.resume = existing_resume.get("resume", "")
            payload.user = user_id
            validated_payload = payload.model_dump()

            update_result = await resume_collection.update_one(
                {"user": user_id}, {"$set": validated_payload}
            )
            if update_result.modified_count == 0:
                raise HTTPException(
                    status_code=500, detail="Failed to update the resume"
                )

            return {"message": "Resume updated successfully", "data": validated_payload}

        except ValidationError as ve:
            raise HTTPException(status_code=422, detail=ve.errors())
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Unexpected error occurred: {str(e)}"
            )

    async def delete_resume(resume_id: str):
        current_db = db.get_database()
        resume_collection = current_db["resume"]

        if not ObjectId.is_valid(resume_id):
            raise HTTPException(status_code=400, detail="Invalid resume ID format")

        delete_result = await resume_collection.delete_one({"_id": ObjectId(resume_id)})
        if delete_result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Resume not found")
        return {"message": "Resume deleted successfully"}

    # education , skill,

    ###########generate_json_resume###############
    async def generate_json_resume(request):
        current_db = db.get_database()
        resume_collection = current_db["resume"]
        user_id = request.state.user_id
        print("======================", user_id)
        try:
            existing_resume = await resume_collection.find_one({"user": user_id})
            if not existing_resume.get("resume") and not existing_resume.get(
                "linkedin_resume"
            ):
                raise HTTPException(
                    status_code=400,
                    detail={
                        'Please upload both "resume" and "linkedin resume" to proceed further'
                    },
                )

            prompt_to_chatgpt = (
                existing_resume.get("linkedin_resume")
                + existing_resume.get("resume")
                + resume_get_prompt
            )
            response_str = invoke(prompt_to_chatgpt)
            print(
                "----------prompt of ----------------\n",
                prompt_to_chatgpt,
                "----------result chatgpt ----------------\n",
                response_str,
            )

            response_json = extract_json_from_string(response_str)

            response_json["user"] = user_id
            response_json["linkedin_resume"] = existing_resume.get("linkedin_resume")
            response_json["resume"] = existing_resume.get("resume")
            result = await resume_collection.update_one(
                {"user": user_id},
                {"$set": Resume(**response_json).model_dump()},
                upsert=True,
            )

            return {"message": "File uploaded successfully", "data": response_json}
        except HTTPException as exc:
            raise exc
        except Exception as e:
            return HTTPException(
                status_code=500, detail=f"An error occurred:---- {str(e)}"
            )
