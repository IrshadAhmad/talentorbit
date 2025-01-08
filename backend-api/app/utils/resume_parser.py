import pdfplumber
from docx import Document
from fastapi import HTTPException

def extract_text_from_pdf(file_path: str) -> str:
    content = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                content += page.extract_text() + "\n"
    except Exception as e:
        raise HTTPException(status_code=422,detail=f"Error reading PDF file. The file is corrupted or invalid.: {str(e)}")
    return content

def extract_text_from_doc(file_path: str) -> str:
    content = ""
    try:
        doc = Document(file_path)
        for paragraph in doc.paragraphs:
            content += paragraph.text + "\n"
    except Exception as e:
        raise HTTPException(status_code=422,detail=f"Error reading DOC/DOCX file:  The file is corrupted or invalid.: {str(e)}")

    return content


def merge_resume_data(existing_data: dict, new_data: dict) -> dict:
    """
    Merges existing resume data with new resume data.
    Keeps old values if new values are empty.
    """
    if not existing_data:  # Handle cases where existing data is None
        return new_data

    for key, value in new_data.items():
        if key in existing_data:
            if isinstance(value, dict) and isinstance(existing_data[key], dict):
                # Recursively merge dictionaries
                existing_data[key] = merge_resume_data(existing_data[key], value)
            elif isinstance(value, list) and isinstance(existing_data[key], list):
                # Merge lists (extend with new data or keep old if new is empty)
                if value:  # Use the new list if it's not empty
                    existing_data[key] = value
            elif value or value == 0:  # Update scalar values only if new value is non-empty
                existing_data[key] = value
        else:
            # Add new key-value pair if not present in existing data
            existing_data[key] = value

    return existing_data
