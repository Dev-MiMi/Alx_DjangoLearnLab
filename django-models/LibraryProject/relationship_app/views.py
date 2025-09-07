from django.shortcuts import render
from .models import Book
from .models import Library

# Create your views 

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetails(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # This ensures your template receives 'library'

