from typing import Any
from fastapi.responses import JSONResponse


def custom_response(
        success: bool,
        status_code: int,
        data: Any,
        message: str
):
    return JSONResponse({
        'success': success,
        'status_code': status_code,
        'data': data,
        'message': message
    }, status_code=status_code)
