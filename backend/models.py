from sqlalchemy import Column, Integer, String, Float, Boolean
from backend.database import Base

class Book(Base):
    __tablename__ = "books"
    book_id = Column(Integer, primary_key= True, index= True)
    title = Column(String)
    price = Column(Float)
    star_rating = Column(Integer)
    genre = Column(String)
    publication_year = Column(Integer)
    page_count = Column(Integer)
    available = Column(Boolean)