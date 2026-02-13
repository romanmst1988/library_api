import factory
from apps.authors.models import Author
from apps.books.models import Book
from apps.borrowings.models import BorrowRecord
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    password = factory.PostGenerationMethodCall("set_password", "password123")
    role = "reader"


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = factory.Sequence(lambda n: f"Author {n}")


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Sequence(lambda n: f"Book {n}")
    genre = "Fiction"
    published_year = 2020
    available_copies = 5

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for author in extracted:
                self.authors.add(author)
        else:
            self.authors.add(AuthorFactory())


class BorrowFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BorrowRecord

    user = factory.SubFactory(UserFactory)
    book = factory.SubFactory(BookFactory)
    return_due = "2030-01-01"
