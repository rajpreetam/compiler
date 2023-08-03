from fastapi import HTTPException, status


class CustomInternalServerException(HTTPException):
    def __init__(
            self,
            detail: str = 'Internal Server Error',
            headers: dict = None
    ):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
            headers=headers
        )
