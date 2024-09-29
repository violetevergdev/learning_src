from src.db.db_connection import engine, Session, Base
from src.models.models import Workers


def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def insert_data():
    worker_bob = Workers(username='Bob')
    worker_max = Workers(username='Max')
    with Session() as session:
        session.add_all([worker_bob, worker_max])
        session.commit()
