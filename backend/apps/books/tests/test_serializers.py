import pytest
from apps.books.serializers import BookSerializer
from model_bakery import baker
from apps.books.models import Book


@pytest.mark.django_db
def test_book_serializer():
    book = baker.make(Book)

    serializer = BookSerializer(book)

    assert "id" in serializer.data
