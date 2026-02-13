import pytest
from tests.factories import BookFactory

pytestmark = pytest.mark.django_db


def test_books_list(auth_client):
    BookFactory.create_batch(3)

    response = auth_client.get("/api/books/")

    assert response.status_code == 200
    assert len(response.data) == 3


def test_create_book(auth_client):
    data = {
        "title": "New Book",
        "genre": "Sci-Fi",
        "published_year": 2024,
        "available_copies": 2,
        "authors": []
    }

    response = auth_client.post("/api/books/", data)

    assert response.status_code in [200, 201]
