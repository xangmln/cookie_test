from fastapi import APIRouter,status,Depends
from sqlalchemy.orm import Session

from typing import Annotated

from api.utils.dependency import get_db
from api.schemas.user import UserCreate
from api.services.user import user_service
from api.responses.success_response import success_response

db_dependency = Annotated[Session,Depends(get_db)]

auth = APIRouter(prefix="/auth", tags=["auth"])

@auth.post("/register", status_code=status.HTTP_201_CREATED)
async def user_register(user: UserCreate, db : db_dependency):
    data = user_service.user_create(user,db)

    return success_response(
        status_code=status.HTTP_201_CREATED,
        message="User created successfully",
        data = data
    )