from django.contrib import admin
from django.urls import path
from api.views import AuthorListCreateView, BookListCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', AuthorListCreateView.as_view(), name='author-list'),
    path('books/', BookListCreateView.as_view(), name='book-list'),
]
