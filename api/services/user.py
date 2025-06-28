import os
from dotenv import load_dotenv

from sqlalchemy.orm import Session

from passlib.context import CryptContext
from typing import Annotated

from api.utils.dependency import get_db
from api.models.user import User
from api.models.refresh_token import RefreshToken
from api.responses.success_response import success_response
from api.schemas.user import UserCreate

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

db_dependency = Annotated[Session,get_db]

class UserService:



user_service = UserService()