import pytest
from backend.apps.books.models import Book

@pytest.mark.django_db
def test_create_book():
    book = Book.objects.create(
        title="Test Book",
        genre="Sci-Fi",
        published_year=2020,
        available_copies=5,
    )

    assert book.title == "Test Book"
    assert book.available_copies == 5
