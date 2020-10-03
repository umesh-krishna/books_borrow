from django.urls import path
from books import views


urlpatterns = [
    path('list/', views.BooksListAPI.as_view()),
    path('borrow/', views.BookBorrowAPI.as_view()),
]
