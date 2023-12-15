from fastapi import FastAPI, Depends, HTTPException, status, Response
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
    return books

#return a single book
@app.get('/books/{book_id}')
def books(book_id: int, db: Session= Depends(get_db)):
    book= db.query(Books).filter(Books.id == book_id).first()

    return book

#create/add a book
@app.post('/books')
def create(book: BookSchema, db: Session = Depends(get_db)):
    new_book = Books(**book.model_dump())

    #add book to the transaction
    db.add(new_book)
    #commit the transaction
    db.commit()
    #get evet from db again
    db.refresh(new_book)
    return {"message":"Book added succesfully", "book": new_book}

#update a book
@app.patch('/books/{book_id}')
def update_book(book_id: int,updated_data: dict, db:Session= Depends(get_db)):
    book_to_update= db.query(Books).filter(Books.id == book_id).first()

    #check if it exists
    if book_to_update == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
                            detail=f"Book {book_id} does not exist")
    else:
        #convert the data to a dictionary
        updated_data = {key: value for key, value in updated_data.items()}

        db.query(Books).filter(Books.id == book_id).update(updated_data)
        db.commit()


    return {"message": f"Book {book_id} updated successfully"}

#delete a book
@app.delete('/books/{book_id}')
def delete_book(book_id: int, db: Session= Depends(get_db)):
    book_to_delete = db.query(Books).filter(Books.id == book_id).first()

    if book_to_delete == None :
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
                            detail=f"Book {book_id} does not exist")
    else:
        db.delete(book_to_delete)
        #commit transaction
        db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
