from datetime import datetime
from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey, text
from src.db.db_connection import Base, str200

import enum

intpk = Annotated[int, mapped_column(primary_key=True)]
cu_at = Annotated[datetime, mapped_column(server_default=text("CURRENT_TIMESTAMP"))]

class Workers(Base):
    __tablename__ = 'workers'

    id: Mapped[intpk]
    username: Mapped[str]


class Workload(enum.Enum):
    parttime = 'parttime'
    fulltime = 'fulltime'


class Resumes(Base):
    __tablename__ = 'resumes'

    id: Mapped[intpk]
    title: Mapped[str200]
    compensation: Mapped[int | None]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete='CASCADE'))
    created_at: Mapped[cu_at]
    updated_at: Mapped[cu_at]
