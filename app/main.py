from fastapi import FastAPI
from app.core.config import settings


app = FastAPI(title=settings.app_name, version=settings.app_version)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": f"{settings.app_name} is running",
        "environment": settings.app_env,
    }
