from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def add_cors_middleware(app: FastAPI):
    """
    Adds CORS middleware to the FastAPI app to allow cross-origin requests.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Adjust origins as needed for security
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
