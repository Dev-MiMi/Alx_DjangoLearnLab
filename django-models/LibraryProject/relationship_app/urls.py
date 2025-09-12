from django.urls import path
from .views import list_books, LibraryDetailView
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
        path('books/', list_books, name='list_books'),
        path('books/add/', views.add_book, name='add_book', name='add_book'),
        path('books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
        path('books/<int:book_id>/delete/', views.delete_book, name='delete_book'),
        path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
        path('register/', views.register, name='register'),
        path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
        path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
