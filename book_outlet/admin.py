from django.contrib import admin

from .models import Author, Book


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("title", "rating")
    list_display = ("title", "author")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    list_filter = ("last_name", )


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)