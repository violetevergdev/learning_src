from typing import Annotated

from sqlalchemy import create_engine, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('sqlite:///albums.db', echo=False)
Session = sessionmaker(engine)

str_256 = Annotated[str, 256]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }

    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        columns = []

        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                columns.append(f'{col} = {getattr(self, col)}')


        return f'<{self.__class__.__name__} {','.join(columns)}>'
