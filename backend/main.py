from fastapi import FastAPI, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
import backend.models as models, backend.schemas as schemas
import backend.database as database

get_db = database.get_db
app = FastAPI()


@app.get('/books', response_model=schemas.APIResponse[List[schemas.ShowBook]],tags = ["Book"])
def get_books(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    if not books:
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'book with the id {id} is not avaialable')
        return {
            "success": False,
            "message": "Couldn't fetch Books",
            "data": None,
            "errors": ["No Books Found."]
        }
    return{
        "success": True,
        "message": "Book Fetched Successfully",
        "data": books,
        "errors": None
    }

@app.get('/books/{id}', response_model =schemas.APIResponse[schemas.ShowBook], tags = ["Book"])
def get_book_id(id: int, db: Session = Depends(get_db)):
    books = db.query(models.Book).filter(models.Book.book_id == id).first()
    if not books:
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'book with the id {id} is not avaialable')
        return {
            "success": False,
            "message": f"Book with id {id} not found",
            "data": None,
            "errors": {"id": ["Invalid Book ID"]}
        }
    return{
        "success": True,
        "message": "Book Fetched Successfully",
        "data": books,
        "errors": None
    }
