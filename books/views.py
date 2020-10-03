from django.shortcuts import render
from rest_framework import views as rest_views, generics
from books.models import Book, UserBookAllocation
from books import serializers
from books_inventory.decorators import login_required
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse


class BooksListAPI(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer


class BookBorrowAPI(rest_views.APIView):
    authentication_classes = (TokenAuthentication,)

    @login_required
    def get(self, request):
        books = UserBookAllocation.objects.filter(status=1, user=request.user).values('book_id', 'book__name')
        result = [{'book_id': x['book_id'], 'book_name': x['book__name']} for x in books]
        return JsonResponse({'books': result})

    @login_required
    def post(self, request):
        data = request.data
        if 'book_id' not in data:
            return JsonResponse({'message': 'Bad Request'}, status=400)
        try:
            book = Book.objects.get(id=data.get('book_id'))
        except book.DoesNotExist:
            return JsonResponse({'message': 'Invalid Book id'}, status=404)
        if book.count > 0:
            book.count -= 1
            book.save()
            UserBookAllocation.objects.create(
                book=book,
                user=request.user
            )
            return JsonResponse({'message': 'Success'}, status=200)
        else:
            return JsonResponse({'message': 'No stock'}, status=404)
