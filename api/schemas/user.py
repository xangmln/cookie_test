from pydantic import BaseModel,EmailStr,Field

from typing import Literal, Optional
from datetime import datetime

class UserBase(BaseModel):
    username : str = Field(min_length=2,max_length=20),
    email : EmailStr
    role : Literal["admin", "user"] = "user"

class UserCreate(UserBase):
    password : str

class UserLogin(BaseModel):
    email : EmailStr
    password: str

class UserCreateResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    access_token: str
    expiry: datetime
