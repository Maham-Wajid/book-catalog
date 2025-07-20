from sqlalchemy import Column, Integer, String
from .database import Base


class Book(Base):
    """
    SQLAlchemy ORM model representing a book in the database.
    Attributes:
        id (int): Primary key, unique identifier for the book.
        title (str): Title of the book (required).
        author (str): Author of the book (required).
        published_year (int): Year the book was published (required).
        summary (str, optional): Short summary or description of the book.
    """

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    published_year = Column(Integer, nullable=False)
    summary = Column(String, nullable=True)
