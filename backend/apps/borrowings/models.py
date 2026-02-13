from django.conf import settings
from django.db import models


class BorrowRecord(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)
    return_due = models.DateField()
    returned_at = models.DateTimeField(null=True, blank=True)
