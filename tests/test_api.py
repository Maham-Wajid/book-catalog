from fastapi.testclient import TestClient
from app.main import app

# Create a test client for FastAPI integration tests
client = TestClient(app)


def test_create_and_get_book():
    """
    Test that a book can be created via the API and then retrieved by ID.
    """
    response = client.post(
        "/books/",
        json={"title": "API Test", "author": "Tester", "published_year": 2021},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "API Test"
    book_id = data["id"]

    # Fetch the same book by ID
    get_resp = client.get(f"/books/{book_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == "API Test"


def test_delete_book():
    """
    Test that a book can be deleted via the API and is no longer accessible.
    """
    res = client.post(
        "/books/", json={"title": "To Delete", "author": "A", "published_year": 2020}
    )
    book_id = res.json()["id"]

    # Delete the book
    del_res = client.delete(f"/books/{book_id}")
    assert del_res.status_code == 200
    assert del_res.json()["message"] == f"Book with ID {book_id} deleted successfully."

    # Ensure it's no longer retrievable
    not_found = client.get(f"/books/{book_id}")
    assert not_found.status_code == 404
