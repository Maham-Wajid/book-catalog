from sqlalchemy.orm import Session
from . import models, schemas


def get_book(db: Session, book_id: int):
    """
    Retrieve a single book by its ID.
    Args:
        db (Session): SQLAlchemy session.
        book_id (int): The ID of the book to retrieve.
    Returns:
        Book instance if found, otherwise None.
    """
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_books(db: Session):
    """
    Retrieve all books from the database.
    Args:
        db (Session): SQLAlchemy session.
    Returns:
        List of all Book instances.
    """
    return db.query(models.Book).all()


def create_book(db: Session, book: schemas.BookCreate):
    """
    Create a new book record in the database.
    Args:
        db (Session): SQLAlchemy session.
        book (BookCreate): Pydantic model containing book data.
    Returns:
        The created Book instance.
    """
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, db_book: models.Book, updates: schemas.BookUpdate):
    """
    Fully update an existing book with new data (PUT behavior).
    Args:
        db (Session): SQLAlchemy session.
        db_book (Book): Existing book instance to update.
        updates (BookCreate): New book data (all fields required).
    Returns:
        The updated Book instance.
    """
    for key, value in updates.dict().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book


def partial_update_book(db: Session, db_book: models.Book, updates: schemas.BookUpdate):
    """
    Partially update fields of an existing book (PATCH behavior).
    Args:
        db (Session): SQLAlchemy session.
        db_book (Book): Existing book instance to update.
        updates (BookUpdate): Partial data with only the fields to change.
    Returns:
        The updated Book instance.
    """
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(db_book, field, value)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, db_book: models.Book):
    """
    Delete a book from the database.
    Args:
        db (Session): SQLAlchemy session.
        db_book (Book): Book instance to delete.
    Returns:
        None
    """
    db.delete(db_book)
    db.commit()
