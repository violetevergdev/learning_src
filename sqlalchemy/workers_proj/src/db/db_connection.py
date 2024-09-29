from typing import Annotated

from sqlalchemy import create_engine, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('sqlite:///albums.db', echo=True)
Session = sessionmaker(engine)

str200 = Annotated[str, 200]


class Base(DeclarativeBase):
    type_annotation_map = {
        str200: String(200)
    }
