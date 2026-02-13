import pytest
from model_bakery import baker
from apps.books.models import Book


@pytest.mark.django_db
def test_create_book():
    book = baker.make(Book)

    assert book.id is not None
    assert str(book) != ""
