from fastapi import status
from ..schemas import UserRequestBody
from core.utils.custom_exceptions import CustomInternalServerException
from core.utils.custom_response import custom_response
from sqlalchemy.orm import Session
from ..queries.register_user_query import (
    register_user_query,
    is_email_unique,
    is_username_unique
)


def register_user_service(db: Session, data: UserRequestBody):
    try:
        if not is_email_unique(db, data.email):
            return custom_response(
                success=False,
                status_code=status.HTTP_400_BAD_REQUEST,
                data=None,
                message='This email is already been registered by someone'
            )
        if not is_username_unique(db, data.username):
            return custom_response(
                success=False,
                status_code=status.HTTP_400_BAD_REQUEST,
                data=None,
                message='This username is already taken'
            )
        if len(data.password) < 8:
            return custom_response(
                success=False,
                status_code=status.HTTP_400_BAD_REQUEST,
                data=None,
                message='Password must be 8 or more character long'
            )
        if data.password != data.confirm_password:
            return custom_response(
                success=False,
                status_code=status.HTTP_400_BAD_REQUEST,
                data=None,
                message='Passwords must match'
            )
        user = register_user_query(db, data)
        if user is not None:
            return {
                'success': True,
                'status_code': status.HTTP_201_CREATED,
                'data': user,
                'message': 'User registered successfully'
            }
        raise CustomInternalServerException
    except Exception as e:
        print(e)
        raise CustomInternalServerException
