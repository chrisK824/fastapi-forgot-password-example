from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List
from permissions.roles import Role


class UserSignUp(BaseModel):
    email: EmailStr
    password: Optional[str]
    name: str
    surname: Optional[str] = None
    role: Role


class UserUpdate(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    role: Optional[Role]


class UserUpdateMe(BaseModel):
    name: Optional[str]
    surname: Optional[str]


class UserChangePassword(BaseModel):
    old_password: str
    new_password: str


class User(UserSignUp):
    register_date: datetime

    class Config:
        from_attributes = True


class UserOut(BaseModel):
    email: EmailStr
    name: Optional[str]
    surname: Optional[str]
    role: Role
    register_date: datetime

    class Config:
        from_attributes = True


class UserMe(BaseModel):
    email: EmailStr
    name: Optional[str]
    surname: Optional[str]
    register_date: datetime
    role: Role
    permissions: List[str]


class Token(BaseModel):
    access_token: str
    token_type: str
