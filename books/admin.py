from django.contrib import admin
from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = ('name', 'author')
    list_display = ('name', 'author', 'count')
