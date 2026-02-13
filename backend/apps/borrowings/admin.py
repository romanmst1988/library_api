from django.contrib import admin
from .models import BorrowRecord


@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "book",
        "borrowed_at",
        "return_due",
        "returned_at",
    )
    list_filter = ("borrowed_at", "return_due", "returned_at")
    search_fields = ("user__username", "book__title")



# Register your models here.
# admin.site.register(BorrowRecord)