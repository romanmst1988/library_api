import factory

from backend.apps.books.models import Book


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = "Test"
    genre = "Drama"
    published_year = 2020
    available_copies = 3
