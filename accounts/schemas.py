from pydantic import BaseModel


class CustomResponse(BaseModel):
    success: bool
    status_code: int
    message: str


class UserBase(BaseModel):
    email: str
    username: str
    first_name: str | None = None
    last_name: str | None = None


class UserRequestBody(UserBase):
    password: str
    confirm_password: str


class UserResponseBodyData(UserBase):
    id: int


class UserResponseBody(CustomResponse):
    data: UserResponseBodyData | None = None

    class Config:
        from_attributes = True


class UserLoginRequestBody(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access: str
    refresh: str


class UserLoginResponseBodyData(BaseModel):
    token: Token
    user: UserResponseBodyData


class UserLoginResponseBody(CustomResponse):
    data: UserLoginResponseBodyData
