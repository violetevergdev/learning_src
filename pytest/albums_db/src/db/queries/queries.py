from src.models.albums_models import Albums
from src.db.db_conn import Base, engine, Session

from sqlalchemy import select, delete, insert


class AlbumsQueries:

    @classmethod
    def create_tables(cls):
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    @classmethod
    def add_album(cls, data: dict):
        stmt = insert(Albums).values(**data).returning(Albums)
        with Session() as session:
            new_album = session.execute(stmt)
            session.commit()
            return new_album.scalar()

    @classmethod
    def select_all_album(cls):
        query = select(Albums)
        with Session() as session:
            result = session.execute(query)
            albums = result.scalars().all()
            return albums

    @classmethod
    def get_album_by_id(cls,album_id: int = 1):
        query = select(Albums).filter(Albums.id == album_id)
        with Session() as session:
            res = session.execute(query)
            album = res.scalar_one_or_none()
            return album


    @classmethod
    def update_album(cls, album_id: int = 1, arg_for_update: str = 'title',
                     new_value: str | int = 'New_Title'):
        if arg_for_update == 'rating' and not isinstance(new_value, int):
            try:
                new_value = int(new_value)
            except Exception:
                raise ValueError("Новое значение должно быть числом")
        elif arg_for_update in ('title', 'author') and not isinstance(new_value, str):
            try:
                new_value = str(new_value)
            except Exception:
                raise ValueError("Новое значение должно быть строкой")
        try:
            with Session() as session:
                album = session.get(Albums,  album_id)
                if arg_for_update == 'rating':
                    album.rating = new_value
                elif arg_for_update == 'title':
                    album.title = new_value
                elif arg_for_update == 'author':
                    album.author = new_value

                session.commit()
                return album
        except Exception:
            raise AttributeError("Нет записи с таким идентификатором")

    @classmethod
    def delete_album_by_id(cls, album_id: int):
        stmt = delete(Albums).where(Albums.id == album_id)

        with Session() as session:
            session.execute(stmt)
            session.commit()