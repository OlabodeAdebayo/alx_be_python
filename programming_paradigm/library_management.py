class Book:
    #Represents a book with a title, author, and availability status.

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  

    def check_out(self):
        #Mark the book as checked out.
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        #Mark the book as returned.
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        #Check if the book is available for checkout.
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    #Manages a collection of books.

    def __init__(self):
        self._books = []

    def add_book(self, book):
        #Add a Book instance to the library.
        self._books.append(book)

    def check_out_book(self, title):
        # Mark a book with the given title as checked out.
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"'{title}' has been checked out.")
                return
        print(f"Sorry, '{title}' is not available for checkout.")

    def return_book(self, title):
        #Return a book with the given title.
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"'{title}' was not checked out or does not exist in the library.")

    def list_available_books(self):
        #List all books that are currently available.
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(book)

