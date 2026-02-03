from pydantic import BaseModel
from typing import List, Optional, Generic, TypeVar, Any

T = TypeVar("T")

class APIResponse(BaseModel, Generic[T]):
    success: bool
    message: str
    data: Optional[T] = None
    errors: Optional[Any] = None

class Book(BaseModel):
    book_id: int
    title: str
    price: float
    star_rating: int
    genre: str
    publication_year: int
    page_count: int
    available: bool

class ShowBook(Book):
    book_id: int
    title: str
    price: float
    star_rating: int
    genre: str
    publication_year: int
    page_count: int
    available: bool
    class Config():
       from_attributes = True
