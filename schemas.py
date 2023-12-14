#this allows us to create schemas of what the app accepts
from pydantic import BaseModel


class BookSchema(BaseModel):
    title: str
    author: str
    image: str
    genre: str
    price: int
    added_at: str
