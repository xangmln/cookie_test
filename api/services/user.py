import os
from dotenv import load_dotenv

from fastapi import HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session

from passlib.context import CryptContext
from typing import Annotated

from api.utils.dependency import get_db
from api.models.user import User
from api.models.refresh_token import RefreshToken
from api.responses.success_response import success_response
from api.schemas.user import UserCreate

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

db_dependency = Annotated[Session,Depends(get_db)]

class UserService:
    def user_create(self,user: UserCreate, db : db_dependency):
        if self.exists(db, user.email):
            raise HTTPException(status.HTTP_400_BAD_REQUEST,"User with email already exist")
        
        hashed_password = self.hash_password(user.password)
        user.password = hashed_password
        user = User(**user.model_dump())

        db.add(user)
        db.commit()
        db.refresh(user)

        user = jsonable_encoder(
            self.get_user_detail(db=db, user_id=user.id), exclude={"password"}
        )

        response = {
            "user": user
        }

        return response


    

    def exists(self, db: db_dependency, email: str) -> bool:
        user = db.query(User).filter(User.email == email).first()

        if user:
            return True

        return False
    
    def hash_password(self,password : str) -> str:
        return bcrypt_context.hash(password)
    
    def get_user_detail(self, db : db_dependency, user_id : str):
        data = db.query(User).filter(User.id==user_id).first()
        if not data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            ) 
        return data




user_service = UserService()