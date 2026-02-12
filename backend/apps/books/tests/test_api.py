import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_books_list():
    user = User.objects.create_user(
        username="test",
        password="12345"
    )

    client = APIClient()
    client.force_authenticate(user=user)

    response = client.get("/api/books/")

    assert response.status_code == 200


@pytest.mark.django_db
def test_create_borrow_record(book, user, client):
    client.force_authenticate(user=user)

    data = {
        "book": book.id,
        "return_due": "2030-01-01"
    }

    response = client.post("/api/borrowings/", data)

    assert response.status_code == 201
