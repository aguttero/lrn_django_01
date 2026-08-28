from django.contrib import admin

from .models import Book, Author, Address, Country


class BookAdmin(admin.ModelAdmin):
    # Adds filter section to admin view
    list_filter = (
        "title",
        "author"
    )

    # Add Columns
    list_display=("author","title",)


# Register your models here.

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
