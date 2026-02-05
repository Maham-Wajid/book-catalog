from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, get_db

# Create database tables on app startup
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Book Catalog API",
    description="A simple CRUD API for managing a book catalog",
    version="1.0.0"
)

# Add CORS middleware to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/books/", response_model=list[schemas.BookResponse])
async def get_books(db: Session = Depends(get_db)):
    """
    Retrieve all books from the catalog (async endpoint).
    Returns:
        List of BookResponse models.
    """
    return crud.get_books(db)


@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a single book by its ID.
    Args:
        book_id (int): The ID of the book to retrieve.
    Returns:
        BookResponse if found.
    Raises:
        HTTPException: If book is not found.
    """
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(
            status_code=404, detail=f"Book with ID {book_id} not found!"
        )
    return db_book


@app.post("/books/", response_model=schemas.BookResponse, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    """
    Create a new book entry.
    Args:
        book (BookCreate): Payload containing title, author, year, and summary.
    Returns:
        The created BookResponse.
    """
    return crud.create_book(db, book)


@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(
    book_id: int, updates: schemas.BookUpdate, db: Session = Depends(get_db)
):
    """
    Fully update a book (PUT). All fields are expected.
    Args:
        book_id (int): The ID of the book to update.
        updates (BookUpdate): Payload with all fields.
    Returns:
        Updated BookResponse.
    Raises:
        HTTPException: If book is not found.
    """
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(
            status_code=404, detail=f"Book with ID {book_id} not found!"
        )
    return crud.update_book(db, db_book, updates)


@app.patch("/books/{book_id}", response_model=schemas.BookResponse)
def partial_update_book(
    book_id: int, updates: schemas.BookUpdate, db: Session = Depends(get_db)
):
    """
    Partially update a book (PATCH). Only provided fields are updated.
    Args:
        book_id (int): The ID of the book to update.
        updates (BookUpdate): Payload with optional fields.
    Returns:
        Updated BookResponse.
    Raises:
        HTTPException: If book is not found.
    """
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(
            status_code=404, detail=f"Book with ID {book_id} not found!"
        )
    return crud.partial_update_book(db, db_book, updates)


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """
    Delete a book by its ID.
    Args:
        book_id (int): ID of the book to delete.
    Returns:
        204 No Content with message if successful.
    Raises:
        HTTPException: If book is not found.
    """
    db_book = crud.get_book(db, book_id)
    if not db_book:
        raise HTTPException(
            status_code=404, detail=f"Book with ID {book_id} not found!"
        )
    crud.delete_book(db, db_book)
    return {"message": f"Book with ID {book_id} deleted successfully."}
