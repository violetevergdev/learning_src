from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('sqlite:///albums.db', echo=True, connect_args={"check_same_thread": False})
Session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass
    