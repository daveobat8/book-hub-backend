from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Books
from schemas import BookSchema
#initialize it
app= FastAPI()

#define a route
@app.get('/')
def index():
    return {"message": "Welcome to my first api"}
#get all books
@app.get('/books')
def books(db: Session = Depends(get_db)):
    books = db.query(Books).all()
    return []

#return a single book
@app.get('/books/{book_id}')
def books():
    return {}

#create/add a book
@app.post('/books')
def create(book: BookSchema):
    print(book)
    return {"message":"Book added succesfully"}

#update a book
@app.patch('/books/{book_id}')
def update_book(book_id: int):
    return {"message": f"Book {book_id} added successfully"}

#delete a book
@app.delete('/books/{book_id}')
def delete_book(book_id: int):
    return {"message": f"Book {book_id} deleted succesfully"}
