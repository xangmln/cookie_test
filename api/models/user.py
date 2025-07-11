from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from enum import Enum

from api.models.abstract import AbstractBase

class RoleEnum(Enum):
    user = 'user'
    admin = 'admin'


class User(AbstractBase):
    __tablename__ = "user"


    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(SQLAlchemyEnum(RoleEnum),default=RoleEnum.user)

    refresh_tokens = relationship("RefreshToken", back_populates="user", cascade="all, delete-orphan")

    def __str__(self) -> str:
        return self.username

