import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app import crud, models, schemas

# Use in-memory SQLite for isolated, fast unit testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture
def db():
    """
    Fixture to create a fresh in-memory SQLite database for each test.
    Yields:
        SQLAlchemy session scoped to the test function.
    """
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_create_book(db):
    """Test that a book can be created and returns a valid ID and correct data."""
    book_in = schemas.BookCreate(
        title="Test Book", author="Test Author", published_year=2020
    )
    book = crud.create_book(db, book_in)
    assert book.id is not None
    assert book.title == "Test Book"
    assert book.author == "Test Author"


def test_get_book(db):
    """Test that a book can be fetched by ID after creation."""
    book = crud.create_book(
        db, schemas.BookCreate(title="Book A", author="A", published_year=2021)
    )
    fetched = crud.get_book(db, book.id)
    assert fetched is not None
    assert fetched.title == "Book A"


def test_get_books(db):
    """Test that multiple books can be retrieved from the database."""
    crud.create_book(
        db, schemas.BookCreate(title="Book 1", author="X", published_year=2018)
    )
    crud.create_book(
        db, schemas.BookCreate(title="Book 2", author="Y", published_year=2019)
    )
    books = crud.get_books(db)
    assert len(books) >= 2


def test_update_book(db):
    """Test that a book can be fully updated using new data."""
    book = crud.create_book(
        db, schemas.BookCreate(title="Initial", author="Dev", published_year=2010)
    )
    updates = schemas.BookUpdate(title="Updated Title", published_year=2022)
    updated = crud.update_book(db, book, updates)
    assert updated.title == "Updated Title"
    assert updated.published_year == 2022


def test_delete_book(db):
    """Test that a book can be deleted and is no longer retrievable."""
    book = crud.create_book(
        db, schemas.BookCreate(title="To Remove", author="Z", published_year=2015)
    )
    crud.delete_book(db, book)
    result = crud.get_book(db, book.id)
    assert result is None
