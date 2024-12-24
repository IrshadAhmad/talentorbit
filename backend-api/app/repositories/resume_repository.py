from typing import Optional, List
from app.models.resume_model import Resume

class ResumeRepository:
    @staticmethod
    async def create_resume(resume_data: dict) -> Resume:
        resume = Resume(**resume_data)
        await resume.insert()
        return resume

    @staticmethod
    async def get_resume_by_id(resume_id: str) -> Optional[Resume]:
        return await Resume.get(resume_id)

    @staticmethod
    async def get_all_resumes() -> List[Resume]:
        return await Resume.find_all().to_list()

    @staticmethod
    async def delete_resume(resume_id: str) -> bool:
        resume = await Resume.get(resume_id)
        if resume:
            await resume.delete()
            return True
        return False