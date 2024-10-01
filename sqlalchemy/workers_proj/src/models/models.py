from datetime import datetime
from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, text
from src.db.db_connection import Base, str_256

import enum

intpk = Annotated[int, mapped_column(primary_key=True)]
cu_at = Annotated[datetime, mapped_column(server_default=text("CURRENT_TIMESTAMP"))]

class Workers(Base):
    __tablename__ = 'workers'

    id: Mapped[intpk]
    username: Mapped[str]

    resumes: Mapped[list["Resumes"]] = relationship(
        back_populates="worker",
    )

    resumes_parttime: Mapped[list["Resumes"]] = relationship(
        back_populates="worker",
        primaryjoin="and_(Workers.id == Resumes.worker_id, Resumes.workload == 'parttime')",
        order_by="Resumes.id.desc()",
    )


class Workload(enum.Enum):
    parttime = 'parttime'
    fulltime = 'fulltime'


class Resumes(Base):
    __tablename__ = 'resumes'

    id: Mapped[intpk]
    title: Mapped[str_256]
    compensation: Mapped[int | None]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete='CASCADE'))
    created_at: Mapped[cu_at]
    updated_at: Mapped[cu_at]

    worker: Mapped["Workers"] = relationship(
        back_populates="resumes"
    )
