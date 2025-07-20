# 📚 Book Catalog API — FastAPI Project

A simple CRUD REST API to manage a catalog of books, built with **FastAPI**, **SQLAlchemy**, and **Pydantic**. This project demonstrates model definition, asynchronous endpoints, validation, and testing in a clean FastAPI architecture.

---

## 🚀 Features

- CRUD operations for books
- SQLite database with SQLAlchemy
- Pydantic validation
- One `async` endpoint
- Auto-generated Swagger & ReDoc docs
- Unit and integration tests with Pytest

---

## 📦 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/book-catalog-fastapi.git
cd book-catalog-fastapi
```

### 2. Create a virtual environment
```
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### ▶️ Run the App
```
uvicorn app.main:app --reload
- Visit http://127.0.0.1:8000/docs to explore the Swagger UI.
- Visit http://127.0.0.1:8000/redoc to explore the ReDoc UI.
```

### 🧪 Run Tests
```
pytest tests/
- test_crud.py — unit tests for database logic
- test_api.py — integration tests for API routes
```

---

## 🛠️ Technologies Used
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- Pytest
