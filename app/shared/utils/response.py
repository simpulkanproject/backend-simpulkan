from typing import Any

from fastapi.responses import JSONResponse
from fastapi import status

from app.shared.dto.base_response_dto import BaseResponseDTO


class ResponseFactory:
    @staticmethod
    def success(message: str, data: Any = None) -> JSONResponse:
        return ResponseFactory.__build_response(
            status_code=status.HTTP_200_OK, success=True, message=message, data=data
        )

    @staticmethod
    def created(message: str, data: Any = None) -> JSONResponse:
        return ResponseFactory.__build_response(
            status_code=status.HTTP_201_CREATED,
            success=True,
            message=message,
            data=data,
        )

    @staticmethod
    def not_found(message: str, data: Any = None) -> JSONResponse:
        return ResponseFactory.__build_response(
            status_code=status.HTTP_404_NOT_FOUND,
            success=False,
            message=message,
            data=data,
        )

    @staticmethod
    def bad_request(message: str, data: Any = None) -> JSONResponse:
        return ResponseFactory.__build_response(
            status_code=status.HTTP_400_BAD_REQUEST,
            success=False,
            message=message,
            data=data,
        )

    @staticmethod
    def internal_server_error(message: str = "Internal server error") -> JSONResponse:
        return ResponseFactory.__build_response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            success=False,
            message=message,
            data=None,
        )

    @staticmethod
    def __build_response(
        status_code: int, success: bool, message: str, data: Any = None
    ) -> JSONResponse:
        body = BaseResponseDTO(success=success, message=message, data=data)

        return JSONResponse(status_code=status_code, content=body.model_dump())
