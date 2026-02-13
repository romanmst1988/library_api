from apps.authors.views import AuthorViewSet
from apps.books.views import BookViewSet
from apps.borrowings.views import BorrowRecordViewSet
from apps.users.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("authors", AuthorViewSet)
router.register("books", BookViewSet)
router.register("users", UserViewSet)
router.register("borrowings", BorrowRecordViewSet)

urlpatterns = router.urls
