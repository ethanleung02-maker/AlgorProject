"""
users.py
---------
Defines abstract User class and subclasses.
Demonstrates:
- Abstraction
- Inheritance
- Polymorphism
"""

from abc import ABC, abstractmethod

class User(ABC):
    """
    Abstract base class for all users.
    Cannot be instantiated directly.
    """
    def __init__(self, username):
        self._username = username # Protected attribute


    @abstractmethod
    def get_role(self):
        """
        Abstract method that must be implemented
        by subclasses.
        """
        pass

class Student(User):
    def get_role(self):
        """Student user type"""
        return "Student"
    
class Admin(User):
    """Admin user type"""
    def get_role(self):
        return "Admin"