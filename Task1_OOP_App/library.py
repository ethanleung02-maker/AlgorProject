"""
library.py
-----------
Defines the Library class.
Demonstrates:
- Composition (Library has many Books)
- File handling (JSON storage)
- Exception handling
- Magic method (__len__)
"""

from models import Book
import json

class Library:
    """
    Library class manages a collection of Book objects.
    """
    def __init__(self):
        # Composition: Library contains Book objects
        self.books = []

    # ---------------- Basic Operations ----------------

    def add_book(self, book):
        """Add a Book object to the library"""
        self.books.append(book)

    
    def show_books(self):
        """Print all books"""
        for book in self.books:
            print(book)
    
    def borrow_book(self, title):
        """Borrow a book by title"""
        for book in self.books:
            if book.get_title() == title and book.is_available():
                book.borrow()
                return True
        return False
    
    def return_book(self, title):
        for book in self.books:
            if book.get_title() == title:
                book.return_book()
                return True
        return False
    # ---------------- Magic Method ----------------
    def __len__(self):
        """Return number of books in library""" 
        return len(self.books)
    # ---------------- File Handling ----------------

    def save_to_file(self, filename="library_data.json"):
        """Save library data to JSON file"""
        data = []

        for book in self.books:
            data.append({
                "title": book.get_title(),
                "author": book.get_author(),
                "available": book.is_available()
            })

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename="library_data.json"):
        """Load library data from JSON file"""
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            for item in data:
                book = Book(item["title"], item["author"], "000")
                if not item["available"]:
                    book.borrow()
                self.books.append(book)

        except FileNotFoundError:
            print("No saved data found.")
