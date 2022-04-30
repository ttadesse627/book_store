from django.shortcuts import get_object_or_404, render
from .models import Book
from django.db.models import Avg
# Create your views here.


def index(request):
    books = Book.objects.all().order_by("-rating")
    number_of_books = books.count()
    average_rating = Book.objects.aggregate(Avg(""))
    return render(request, "book_outlet/index.html", {
        "books": books,
        "average_rating": average_rating,
        "number_of_books": number_of_books
    })


def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book-detail.html",{
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling
    })

    # lesson78 - is to be continued!