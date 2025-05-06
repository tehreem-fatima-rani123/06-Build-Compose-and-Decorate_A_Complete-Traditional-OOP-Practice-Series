#11. Class Methods
#Assignment:
#Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0  # Class variable

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def show_total_books(cls):
        print("Total books:", cls.total_books)

# Create book objects
book1 = Book("Python Basics")
book2 = Book("Advanced Python")

# Show total number of books
Book.show_total_books()
