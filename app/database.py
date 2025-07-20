from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database URL for local file-based database
DATABASE_URL = "sqlite:///./books.db"

# Create SQLAlchemy engine with SQLite-specific setting
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session factory bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models
Base = declarative_base()


def get_db():
    """
    Dependency that provides a database session to FastAPI endpoints.
    Yields:
        SQLAlchemy session that is closed after the request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
