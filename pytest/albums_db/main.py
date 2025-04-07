from src.db.queries.queries import AlbumsQueries
from src.models.album_schema import AlbumSchema
from src.models.albums_models import Albums
from src.models.albums_service import AlbumsService as AS, AlbumsService

AlbumsQueries.create_tables()

album = AlbumSchema(
    title='Album',
    author='Artist',
    rating=2,
)

AS.add_album(album)
