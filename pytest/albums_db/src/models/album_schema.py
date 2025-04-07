from pydantic import BaseModel, Field


class AlbumSchema(BaseModel):
    id: int = Field(default=1)
    title: str = Field(default="---")
    author: str = Field(default="---")
    rating: float = Field(default=0, ge=0, le=10)

    def to_dict(self) -> dict:
        return self.model_dump(exclude={"id"})
