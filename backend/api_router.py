from rest_framework.routers import DefaultRouter

from backend.apps.authors.views import AuthorViewSet
from backend.apps.books.views import BookViewSet
from backend.apps.users.views import UserViewSet
from backend.apps.borrowings.views import BorrowRecordViewSet

router = DefaultRouter()

router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
router.register('users', UserViewSet)
router.register('borrowings', BorrowRecordViewSet)

urlpatterns = router.urls
