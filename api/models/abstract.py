from uuid import uuid4
from datetime import datetime

from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from api.utils.datadase import Base

class AbstractBase(Base):
    __abstract__ = True

    id: Mapped[str] = mapped_column(
        String(36), 
        primary_key=True, 
        index=True,
        default=lambda: str(uuid4())
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )