"""
models.py
----------
This module defines the Book class.
It demonstrates:
- Encapsulation
- Class variables
- Class methods
- Static methods
- Magic methods
"""
class Book:
    # Class variable (shared among all instances)
    total_books = 0
    def __init__(self, title, author, isbn):
        """
        Constructor for Book object.
        Validates ISBN before creating the book.
        """
        # Static method used for validation
        if not Book.validate_isbn(isbn):
            raise ValueError("Invalid ISBN!")
        
        # Encapsulated attributes (private variables)
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__available = True

        # Increase class-level counter
        Book.total_books += 1
    
    # ---------------- Getter Methods ----------------

    def get_title(self):
        """Return book title"""
        return self.__title
    
    def get_author(self):
        """Return book author"""
        return self.__author
    
    def is_available(self):
        """Return availability status"""
        return self.__available
    
    # ---------------- Book Actions ----------------

    def borrow(self):
        """
        Borrow the book if available.
        Returns True if successful.
        """
        if self.__available:
            self.__available = False
            return True
        return False
    
    def return_book(self):
        """Return the book and mark as available"""
        self.__available = True
    # ---------------- Magic Methods ----------------    

    def __str__(self):
        """
        Magic method to define string representation.
        """
        status = "Available" if self.__available else "Borrowed"
        return f"{self.__title} by {self.__author} ({status})"
    
    # ---------------- Class & Static Methods ----------------

    @classmethod
    def get_total_books(cls):
        return cls.total_books
    """Return total number of created books"""

    @staticmethod
    def validate_isbn(isbn):
        """
        Validate ISBN format.
        Must be numeric and at least 3 digits.
        """
        return isbn.isdigit() and len(isbn) >= 3