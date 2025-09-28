from django.db import models
from django.utils import timezone

# Author represents a book writer.
# One Author can have many related Book records.
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author’s full name

    def __str__(self):
        return self.name


# Book stores individual book records.
# It has a ForeignKey to Author to establish a one-to-many relationship.
class Book(models.Model):
    title = models.CharField(max_length=200)  # Title of the book
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(
        Author,
        related_name='books',   # Enables reverse access: author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
