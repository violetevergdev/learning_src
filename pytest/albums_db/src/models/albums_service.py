from src.models.album_schema import AlbumSchema
from src.db.queries.queries import AlbumsQueries as AQ
from pydantic import TypeAdapter
from src.db.db_conn import Session
class AlbumsService:

    @classmethod
    def add_album(cls, album: AlbumSchema):
        albums_dict = album.to_dict()

        new_album = AQ.add_album(albums_dict)
        return TypeAdapter(AlbumSchema).dump_python(new_album)

    @classmethod
    def get_album(cls, album_id: int):
        album = AQ.get_album_by_id(album_id)
        return TypeAdapter(AlbumSchema).dump_python(album)

    @classmethod
    def select_all_albums(cls):
        albums = AQ.select_all_album()
        return TypeAdapter(AlbumSchema).dump_python(albums)

    @classmethod
    def update_album(cls, album_id: int, arg: str, value: str | int):
        AQ.update_album(album_id, arg, value)

    @classmethod
    def delete_album(cls, album_id: int):
        AQ.delete_album_by_id(album_id)