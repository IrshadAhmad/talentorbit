from fastapi import UploadFile, HTTPException, status
from pydantic import ValidationError
from app.repositories.resume_repository import save_resume, get_user_resume
from app.models.resume_model import Resume
from app.core.config import settings
import openai
import json

# OpenAI API setup

openai.api_key = settings.OPENAI_KEY

async def extract_resume_content(file: UploadFile) -> dict:
    """
    Extract content from the uploaded resume using OpenAI.
    """
    try:
        content = await file.read()
        prompt = f"""
        Extract the following sections from this resume document:
        Sections: name, contact, summary, education, certifications, skills, work_experiences, projects, achievements, internships, volunteer_works, languages, hobbies_and_interests
        Document: {content.decode()}
        """
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,
        )
        extracted_data = json.loads(response["choices"][0]["text"].strip())
        return extracted_data
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to parse OpenAI response as JSON",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error extracting resume: {str(e)}",
        )
