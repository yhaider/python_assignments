from django.shortcuts import render, redirect
from .models import Author, Review, Book, User
from django.contrib import messages
import re
import bcrypt
from datetime import datetime
# Create your views here.

def home(request):
    return render(request, 'books/home.html')

def add(request):
    return render(request, 'books/add.html')

def process(request):
    if request.POST['author_new']:
        author = Author.objects.create(name = request.POST['author_new'], created_at = datetime.now(), updated_at = datetime.now())
    else:
        author = Author.objects.get(name = request.POST['author'])
    book = Book.objects.create(title = request.POST['title'], authors = author.id, created_at = datetime.now(), updated_at = datetime.now())
    review = Review.objects.create(review = request.POST['review'], rating = request.POST['rating'], book = Book.objects.get(title = request.POST['title']), user = User.objects.get(id = request.session.id))
    return redirect('/books/{}'.format(book.id))

def book(request, number):
    context = {
        'title': Book.objects.get(id=number).title,
        'authors': Book.objects.get(id=number).authors.all(),
    }

    reviews = Book.objects.get(id=number).reviews.all()
    pass

# Create your views here.
