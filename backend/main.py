from fastapi import FastAPI, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
import backend.models as models, backend.schemas as schemas
import backend.database as database
from passlib.context import CryptContext

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

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

@app.post('/user', response_model= schemas.APIResponse[schemas.User], tags = ["User"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == request.email).first()
    
    if existing_user:
        return{
            "success": False,
            "message": "User not created, User exists already",
            "data": existing_user,
            "errors": {"email:": ["Email already registered"]}
        }
    
    user_data = request.model_dump() #standard form structure of converting into the dictionary in user_Data variable of JSON request object
    user_data['password'] = pwd_context.hash(user_data['password']) #im doing this for hashing of password, need to access password key in users table as it comes in form of dictionary. 
    new_user = models.User(**user_data)#now unpacking updated user_data dictionary so that i can store it safely in db
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return{
        "success" : True,
        "message" : "User created successfully",
        "data" : new_user,
        "errors" : None
    }

@app.get('/user/{id}', response_model = schemas.APIResponse[schemas.ShowUser], tags = ["User"])
def get_user(user_id: int, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not user:
        return{
            "success": False,
            "message": f"User with {user_id} not found",
            "data": None,
            "errors": {"UserID": ["User not in Database."]}
        }

    return {
        "success": True,
        "message": "User fetched successfully",
        "data": user,
        "errors": None
    }

@app.put('/user/{id}', response_model = schemas.APIResponse[schemas.ShowUser], tags = ["User"])
def update_user(user_id : int, request: schemas.User, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.user_id == user_id)
    user = user_query.first()
    if not user:
        return{
            "success": False,
            "message": f"User with {user_id} not found",
            "data": None,
            "errors": {"UserID": ["User not in Database. Can't Update User."]}
        }
    update_userr = request.model_dump()
    update_userr['password'] = pwd_context.hash(update_userr['password'])
    user_query.update(update_userr, synchronize_session = False)
    db.commit()
    db.refresh(user)

    return{
        "success" : True,
        "message" : "User updated successfully",
        "data" : user,
        "errors": None

    }

@app.delete('/user/{id}', tags = ["User"])
def delete_user(user_id : int, db:Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.user_id == user_id)
    if not user_query.first():
        return{
            "success": False,
            "message": f"User with {user_id} not found",
            "data": None,
            "errors": {"UserID": ["User not in Database. Can't Delete User."]}
        }
    
    user_query.delete(synchronize_session = False)
    db.commit()
    return {
        "success" : True,
        "message" : f"User with ID {user_id} Deleted successfully",
        "data" : None,
        "errors": None
    }

