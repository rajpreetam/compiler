from typing import Any


def custom_response(
        success: bool,
        status_code: int,
        data: Any,
        message: str
):
    return {
        'success': success,
        'status_code': status_code,
        'data': data,
        'message': message
    }
