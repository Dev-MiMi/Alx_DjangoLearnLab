from relationship_app.models import Author, Book, Library, Librarian

# Authors
achebe = Author.objects.create(name="Chinua Achebe")
orwell = Author.objects.create(name="George Orwell")

# Books
book1 = Book.objects.create(title="Things Fall Apart", author=achebe)
book2 = Book.objects.create(title="Arrow of God", author=achebe)
book3 = Book.objects.create(title="1984", author=orwell)

# Libraries
lib1 = Library.objects.create(name="City Library")

lib1.books.add(book1, book2, book3)

# Librarians (attach to libraries with OneToOneField)
librarian1 = Librarian.objects.create(name="Mary Johnson", library=lib1)

# List all books in a library
library_name = "City Library"
lib = Library.objects.get(name=library_name)

for book in lib.books.all():
    print(book.title)


# Query all books by a specific author
author_name = "Chinua Achebe"
author = Author.objects.get(name=author_name)

books = Book.objects.filter(author=author)
for book in books:
    print(book.title)

# Retrieve the librarian for a library
library_name = "City Library"
library = Library.objects.get(name=library_name)

librarian = Librarian.objects.get(library=library)
print(librarian.name)
