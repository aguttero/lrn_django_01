from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Book


# Create your views here.
def pol(request):
    return render(request, "book_outlet/pol.html")


def index(request):
    books = Book.objects.all()
    print (f"Queryset={books}")
    context = {"books": books}
    return render(request, "book_outlet/index.html", context)


def book_detail(request, id):
    # try:
    #   book = Book.objects.get(pk=id)
    # except:
    #   raise Http404()
    book = get_object_or_404(Book, pk=id)
    print (f"Get Item={book}")
    return render(
        request,
        "book_outlet/book_detail.html",
        {
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
            "is_bestseller": book.is_bestselling,
        }
    )
