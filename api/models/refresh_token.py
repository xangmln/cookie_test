from datetime import datetime

from sqlalchemy import Boolean, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from api.models.abstract import AbstractBase

class RefreshToken(AbstractBase):
    __tablename__ = "refresh_token"

    user_id : Mapped[str] = mapped_column(ForeignKey("user.id"))
    token : Mapped[str] = mapped_column(String(500), nullable=False, unique=True)
    expiry_time: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False
    )
    blacklisted: Mapped[bool] = mapped_column(
        Boolean(), server_default="false", default=False
    )

    user: Mapped["User"] = relationship("User", back_populates="refresh_tokens")

    def __str__(self) -> str:
        return self.token
