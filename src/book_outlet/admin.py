from django.contrib import admin

from .models import Book, BookAuthor, Address, Country


class BookAdmin(admin.ModelAdmin):
    # Adds filter section to admin view
    list_filter = (
        "title",
        "author",
        "last_update"
    )

    # Add Columns
    list_display=("title","author","last_update")
    print (f"type list_display={type(list_display)}")


# Register your models here.

admin.site.register(Book, BookAdmin)
admin.site.register(BookAuthor)
admin.site.register(Address)
admin.site.register(Country)
