#this allows us to create schemas of what the app accepts
from pydantic import BaseModel


class BookSchema(BaseModel):
    title: str
    description: str
    author: str
    image: str
    genre: str
    price: int
    added_at: str

class UserSchema(BaseModel):
    name: str
    phone: str
    email: str

class CatalogueSchema(BaseModel):
    
    title: str
    description: str
    author: str
    image: str
    genre: str
    price: int
    added_at: str
    
