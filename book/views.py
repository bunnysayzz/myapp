from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the Book Home Page!")

BOOKS=[
    {'id':1, 'category':'Fiction', 'title':'3 men in a boat', 'author':'Jerome K. Jerome'},
    {'id':2, 'category':'Fiction', 'title':'The Picture of Dorian Gray', 'author':'Oscar Wilde'},
    {'id':3, 'category':'Fiction', 'title':'The Adventures of Sherlock Holmes', 'author':'Arthur Conan Doyle'},
]

def book_detail(request, book_id):
    book = next((book for book in BOOKS if book['id'] == int(book_id)), None)
    if book:
        return HttpResponse(f"Book: {book['title']} by {book['author']}")
    else:
        return HttpResponse("Book not found", status=404)
    
def category_detail(request, category):
    books_in_category = [book for book in BOOKS if book['category'].lower() == category.lower()]
    if books_in_category:
        book_details = ', '.join(f"{book['title']} by {book['author']}" for book in books_in_category)
        return HttpResponse(f"Books in {category}: {book_details}")
    else:
        return HttpResponse("No books found in this category", status=404)

