import pytest
from tests.factories import BookFactory

pytestmark = pytest.mark.django_db


def test_create_book():
    book = BookFactory()

    assert book.title is not None
    assert book.available_copies > 0
