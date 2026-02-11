from django.contrib import admin
from .models import BorrowRecord

# Register your models here.
@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'book',
        'borrow_date',
        'return_date',
        'is_returned',
    )

    list_filter = (
        'is_returned',
        'borrow_date',
    )

    search_fields = (
        'user__email',
        'book__title',
    )
