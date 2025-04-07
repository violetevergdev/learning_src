import pytest

from src.db.queries.queries import AlbumsQueries as AQ
from src.models.albums_service import AlbumsService as AS
from src.models.albums_models import Albums
from src.models.album_schema import AlbumSchema
from pydantic import TypeAdapter

@pytest.fixture
def albums():
    albums_data = [
        AlbumSchema(
            title='Yeezy',
            author='YE',
            rating=1
        ),

        AlbumSchema(
            title='Man On The Moon',
            author='Kid Cudi'
        )
    ]

    return albums_data

@pytest.fixture
def create_new_table():
    AQ.create_tables()


class TestAlbums:
    @staticmethod
    def test_add_album(albums, create_new_table):

        for album in albums:
            AS.add_album(album)

        assert print(*albums)




