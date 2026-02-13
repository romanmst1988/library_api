import pytest
from model_bakery import baker
from django.urls import reverse
from apps.books.models import Book


@pytest.mark.django_db
def test_get_books(auth_client):
    baker.make(Book, _quantity=3)

    url = reverse("book-list")
    response = auth_client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 3


@pytest.mark.django_db
def test_create_book(auth_client):
    url = reverse("book-list")

    data = {
        "title": "Test book"
    }

    response = auth_client.post(url, data)

    assert response.status_code == 201
