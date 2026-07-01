from fastapi import Request, status
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError


from app.shared.utils.response import ResponseFactory


class ExceptionHandler:
    @staticmethod
    async def handle_http_exception(
        request: Request, exc: HTTPException
    ) -> JSONResponse:
        return ResponseFactory.error(
            status_code=exc.status_code, message=str(exc.detail)
        )

    @staticmethod
    async def handle_validation_exception(
        request: Request,
        exc: RequestValidationError,
    ) -> JSONResponse:
        return ResponseFactory.error(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            message="Validation error",
            data=exc.errors(),
        )

    @staticmethod
    async def handle_internal_exception(
        request: Request,
        exc: Exception,
    ) -> JSONResponse:
        return ResponseFactory.internal_server_error()
