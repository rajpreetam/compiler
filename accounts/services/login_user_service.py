from fastapi import status
from ..schemas import UserLoginRequestBody
from core.utils.custom_exceptions import CustomInternalServerException
from core.utils.custom_response import custom_response
from sqlalchemy.orm import Session


def register_user_login(db: Session, data: UserLoginRequestBody):
    try:
        pass  # TODO: implement login logic
    except Exception as e:
        print(e)
        raise CustomInternalServerException
