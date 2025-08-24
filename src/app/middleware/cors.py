"""
CORS middleware setup.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ...config.settings import settings


def setup_cors(app: FastAPI):
    """Setup CORS middleware for the FastAPI application."""
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["*"],
    )