from backend.tests.factories import AuthorFactory


def test_create_book(auth_client):
    author = AuthorFactory()

    data = {
        "title": "New Book",
        "genre": "Sci-Fi",
        "published_year": 2024,
        "available_copies": 2,
        "authors": [author.id],
    }

    response = auth_client.post("/api/books/", data)

    print(response.data)  # временно

    assert response.status_code in [200, 201]
