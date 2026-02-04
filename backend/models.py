from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

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

class User(Base):
    __tablename__ = "usertable"
    user_id = Column(Integer, primary_key= True, index= True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    gender = Column(String)
