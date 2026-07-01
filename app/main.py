from fastapi import FastAPI
from app.core.config import settings

from app.shared.utils.response import success_response

app = FastAPI(title=settings.app_name, version=settings.app_version)


@app.get("/health")
def health_check():

    return success_response(
        message=f"{settings.app_name} is running",
        data={
            "status": "ok",
            "environment": settings.app_env,
        },
    )
