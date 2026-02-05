# 📚 Book Catalog — FastAPI + Vue.js

A full-stack CRUD application to manage a book catalog with a modern, interactive UI. Built with **FastAPI** backend, **Vue.js** frontend, and **Docker** for easy deployment.

---

## ✨ Features

- 📖 **CRUD Operations** - Create, read, update, delete books
- 🎨 **Vue.js Frontend** - Modern, responsive UI with real-time updates
- 🔄 **RESTful API** - Well-documented FastAPI backend with auto-generated Swagger UI
- 🐳 **Docker Support** - One-command deployment with Docker Compose
- ✅ **Unit & Integration Tests** - Comprehensive test coverage with Pytest
- 🔒 **CORS Enabled** - Ready for cross-origin requests
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile

---

## 🚀 Quick Start

### Option 1: Local Setup (Development)

#### Prerequisites
- Python 3.8+
- pip or conda

#### Steps

1. **Clone the repository**
```bash
git clone https://github.com/your-username/book-catalog.git
cd book-catalog
```

2. **Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the API server** (in one terminal)
```bash
uvicorn app.main:app --reload
```
- API Docs: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

5. **Open the frontend** (in another terminal)
```bash
# Use a simple HTTP server to serve the frontend
python -m http.server 8000 --directory .
```
- Visit http://127.0.0.1:8000/index.html in your browser

---

### Option 2: Docker Compose (Recommended)

#### Prerequisites
- Docker & Docker Compose

#### Steps

1. **Build and run with Docker Compose**
```bash
docker-compose up --build
```

2. **Access the application**
- Frontend: http://localhost:8080
- API: http://localhost:8000/docs

3. **Stop the containers**
```bash
docker-compose down
```

---

## 📦 Project Structure

```
book-catalog/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI application
│   ├── models.py         # SQLAlchemy ORM models
│   ├── schemas.py        # Pydantic schemas
│   ├── crud.py           # CRUD operations
│   └── database.py       # Database configuration
├── tests/
│   ├── test_api.py       # API integration tests
│   └── test_crud.py      # CRUD unit tests
├── index.html            # Vue.js frontend
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker image configuration
├── docker-compose.yml    # Multi-container setup
└── README.md
```

---

## 🛠️ API Endpoints

### Books
- **GET** `/books/` — Get all books
- **GET** `/books/{id}` — Get a specific book
- **POST** `/books/` — Create a new book
- **PUT** `/books/{id}` — Update a book (full)
- **PATCH** `/books/{id}` — Update a book (partial)
- **DELETE** `/books/{id}` — Delete a book

### Example Request
```bash
curl -X POST "http://127.0.0.1:8000/books/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year_published": 1925,
    "summary": "A classic novel set in the Jazz Age."
  }'
```

---

## 🧪 Testing

Run the test suite:
```bash
pytest tests/ -v
```

Run with coverage:
```bash
pytest tests/ --cov=app --cov-report=html
```

---

## 🌐 Deployment

### Deploy Backend to Render

1. Push your code to GitHub
2. Go to [Render.com](https://render.com) and create a new Web Service
3. Connect your GitHub repository
4. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
5. Deploy!

### Deploy Backend to Railway

1. Install Railway CLI: `npm install -g @railway/cli`
2. Login: `railway login`
3. Initialize: `railway init`
4. Deploy: `railway up`

### Deploy Frontend to Vercel or Netlify

1. Commit your `index.html` to GitHub
2. Connect repository to Vercel/Netlify
3. Deploy with one click!

---

## 🔧 Tech Stack

- **Backend**: FastAPI, SQLAlchemy, Pydantic
- **Frontend**: Vue.js 3, HTML5, CSS3
- **Database**: SQLite (can be upgraded to PostgreSQL)
- **Testing**: Pytest
- **Deployment**: Docker, Docker Compose

---

## 📝 License

This project is provided for learning and demonstration purposes.
