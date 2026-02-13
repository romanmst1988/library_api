from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "genre",
        "published_year",
        "available_copies",
    )
    list_filter = ("genre", "published_year")
    search_fields = ("title",)
    filter_horizontal = ("authors",)


# Register your models here.
# admin.site.register(Book)
