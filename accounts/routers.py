from fastapi import APIRouter, Depends
from fastapi import status
from core.utils.custom_exceptions import CustomInternalServerException
from .services.register_user_service import register_user_service
from .schemas import (
    UserRequestBody,
    UserResponseBody,
    UserLoginRequestBody,
    UserLoginResponseBody
)
from sqlalchemy.orm import Session
from core.database import get_db

router = APIRouter(
    prefix='/api/v1/auth',
    tags=['Accounts']
)


@router.post('/register', response_model=UserResponseBody, status_code=status.HTTP_201_CREATED)
async def register_user(data: UserRequestBody, db: Session = Depends(get_db)):
    try:
        return register_user_service(db, data)
    except Exception as e:
        print(e)
        raise CustomInternalServerException


@router.post('/login', response_model=UserLoginResponseBody, status_code=status.HTTP_200_OK)
async def login_user(data: UserLoginRequestBody):
    try:
        pass
    except Exception as e:
        print(e)
        raise CustomInternalServerException
