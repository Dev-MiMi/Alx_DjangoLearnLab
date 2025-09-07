# Authors
achebe = Author.objects.create(name="Chinua Achebe")
orwell = Author.objects.create(name="George Orwell")

# Books
book1 = Book.objects.create(name="Things Fall Apart", author=achebe)
book2 = Book.objects.create(name="Arrow of God", author=achebe)
book3 = Book.objects.create(name="1984", author=orwell)

# Libraries
lib1 = Library.objects.create(name="City Library")
lib2 = Library.objects.create(name="Central Library")

lib1.books.add(book1, book2, book3)
lib2.books.add(book1, book2)

# Librarians (attach to libraries with OneToOneField)
librarian1 = Librarian.objects.create(name="Mary Johnson", library=lib1)
librarian2 = Librarian.objects.create(name="Samuel John", library=lib2)

for book in lib1.books.all():
    print(book.name)
