from typing import Any

from app.shared.dto.base_response_dto import BaseResponseDTO


def success_response(message: str, data: Any = None) -> BaseResponseDTO[Any]:
    return BaseResponseDTO(success=True, message=message, data=data)
