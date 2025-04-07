from sqlalchemy.orm import Mapped, mapped_column
from src.db.db_conn import Base


class Albums(Base):
    __tablename__ = 'albums'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float]
