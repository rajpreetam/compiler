from sqlalchemy.orm import Session
from ..schemas import UserRequestBody
from ..models import User
from ..utils.password_utility import hash_password


def register_user_query(db: Session, data: UserRequestBody):
    try:
        hashed_pwd = hash_password(data.password)
        user = User(
            email=data.email,
            username=data.username,
            first_name=data.first_name,
            last_name=data.last_name,
            password=hashed_pwd
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        print(e)
        db.rollback()
        return None


def is_email_unique(db: Session, email: str):
    try:
        user = db.query(
            User.id
        ).filter(
            User.email == email
        ).one_or_none()
        if user is not None:
            return False
        return True
    except Exception as e:
        print(e)
        return False


def is_username_unique(db: Session, username: str):
    try:
        user = db.query(
            User.id
        ).filter(
            User.username == username
        ).one_or_none()
        if user is not None:
            return False
        return True
    except Exception as e:
        print(e)
        return False
