from PyPDF2 import PdfReader
from docx import Document as DocxDocument
from typing import Dict

def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file_path: str) -> str:
    doc = DocxDocument(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_resume_data(file_path: str) -> Dict:
    """
    Extract relevant information from a resume file (PDF/DOCX).
    """
    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format")

    # Mocked data extraction logic. Replace with NLP or other parsing logic.
    return {
        "name": "John Doe",
        "contact": "john.doe@example.com",
        "summary": ["Experienced software engineer."],
        "education": ["Bachelor's in Computer Science"],
        "certifications": ["AWS Certified Developer"],
        "skills": ["Python", "Django", "FastAPI"],
        "work_experiences": ["3 years at XYZ Corp as a software engineer."],
        "projects": ["E-commerce app development"],
        "achievements": ["Employee of the Year 2023"],
        "internships": ["Summer internship at ABC Inc."],
        "volunteer_works": ["Volunteered at Local Community Center"],
        "languages": ["English", "Spanish"],
        "hobbies_and_interests": ["Cycling", "Reading"]
    }