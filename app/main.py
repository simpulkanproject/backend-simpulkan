from fastapi import FastAPI
from app.core.config import settings

from app.shared.utils.response import ResponseFactory
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError

from app.core.exceptions import ExceptionHandler

app = FastAPI(title=settings.app_name, version=settings.app_version)

app.add_exception_handler(HTTPException, ExceptionHandler.handle_http_exception)
app.add_exception_handler(
    RequestValidationError, ExceptionHandler.handle_validation_exception
)
app.add_exception_handler(Exception, ExceptionHandler.handle_internal_exception)


@app.get("/health")
def health_check():

    return ResponseFactory.success(
        message=f"{settings.app_name} is running",
        data={
            "status": "ok",
            "environment": settings.app_env,
        },
    )
