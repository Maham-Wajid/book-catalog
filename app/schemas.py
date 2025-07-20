from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

# Define the current year to validate published_year input
CURRENT_YEAR = datetime.now().year


class BookBase(BaseModel):
    """
    Base Pydantic model for book data shared between creation and response.
    Attributes:
        title (str): The title of the book (minimum 3 characters).
        author (str): The author's name (minimum 3 characters).
        published_year (int): Year the book was published (validated).
        summary (str, optional): A short summary of the book.
    """

    title: str = Field(..., min_length=3)
    author: str = Field(..., min_length=3)
    published_year: int
    summary: Optional[str] = None

    @validator("published_year")
    def validate_published_year(cls, v):
        """
        Validate that the published year is between 1450 and the current year.
        """
        if v < 1450 or v > CURRENT_YEAR:
            raise ValueError(f"published_year must be between 1450 and {CURRENT_YEAR}")
        return v


class BookCreate(BookBase):
    """
    Schema for creating a new book. Inherits all fields from BookBase.
    """

    pass


class BookUpdate(BaseModel):
    """
    Schema for partially updating a book. All fields are optional.
    """

    title: Optional[str] = None
    author: Optional[str] = None
    published_year: Optional[int] = None
    summary: Optional[str] = None

    @validator("published_year")
    def validate_published_year(cls, v):
        """
        Validate that the published year (if provided) is between 1450 and the current year.
        """
        if v < 1450 or v > CURRENT_YEAR:
            raise ValueError(f"published_year must be between 1450 and {CURRENT_YEAR}")
        return v


class BookResponse(BookBase):
    """
    Schema for returning book data in API responses.
    Includes the book's ID and enables ORM mode to work with SQLAlchemy models.
    """

    id: int

    class Config:
        orm_mode = True
