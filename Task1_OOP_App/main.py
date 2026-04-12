"""
main.py
--------
Main entry point of the Library Management System.

Features:
- GUI using Tkinter
- Role-based login system
- Permission control (Admin vs Student)
- Persistent storage using JSON
- Integration of all modules

Demonstrates:
- OOP integration
- GUI programming
- Event-driven programming
"""

import tkinter as tk
from tkinter import messagebox
from models import Book
from library import Library
from users import Student, Admin

# =========================
# System Initialization
# =========================

library = Library()
library.load_from_file()

current_user = None


# ================= LOGIN =================
def login():
    """
    Handle login process.
    Creates Student or Admin object
    based on selected role.
    """
    global current_user

    username = entry_username.get().strip()
    role = role_var.get()

    if username == "":
        messagebox.showerror("Error", "Please enter username.")
        return

    if role == "Student":
        current_user = Student(username)
    else:
        current_user = Admin(username)

    # Switch frames
    login_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)

    # Update header info
    user_label.config(
        text=f"Logged in as: {current_user._username} ({current_user.get_role()})"
    )

    update_books()


# ================= UPDATE BOOK LIST =================
def update_books():
    """Refresh the book list display"""
    listbox.delete(0, tk.END)
    for book in library.books:
        listbox.insert(tk.END, str(book))

    total_label.config(text=f"Total Books: {len(library)}")


# ================= BORROW =================
def borrow_book():
    """Borrow selected book"""

    selected = listbox.get(tk.ACTIVE)
    if not selected:
        return

    title = selected.split(" by ")[0]

    if library.borrow_book(title):
        messagebox.showinfo("Success", "Book borrowed!")
        library.save_to_file()
    else:
        messagebox.showerror("Error", "Book not available.")

    update_books()


# ================= RETURN =================
def return_book():
    """Return selected book"""

    selected = listbox.get(tk.ACTIVE)
    if not selected:
        return

    title = selected.split(" by ")[0]

    library.return_book(title)
    messagebox.showinfo("Success", "Book returned!")
    library.save_to_file()
    update_books()


# ================= ADD BOOK (admin feature)=================

def add_book():
    """
    Add a new book (Admin only)
    Demonstrates permission control.
    """
    if current_user.get_role() != "Admin":
        messagebox.showerror("Permission Denied", "Only Admin can add books.")
        return

    title = entry_title.get().strip()
    author = entry_author.get().strip()
    isbn = entry_isbn.get().strip()

    if title == "" or author == "" or isbn == "":
        messagebox.showerror("Error", "All fields required.")
        return

    try:
        book = Book(title, author, isbn)
        library.add_book(book)
        library.save_to_file()

        entry_title.delete(0, tk.END)
        entry_author.delete(0, tk.END)
        entry_isbn.delete(0, tk.END)

        messagebox.showinfo("Success", "Book added!")
        update_books()

    except ValueError:
        messagebox.showerror("Error", "Invalid ISBN.")


# ================= MAIN WINDOW (GUI set-up)=================
root = tk.Tk()
root.title("Library Management System")
root.geometry("700x550")
root.configure(bg="#f4f6f7")


# ================= LOGIN FRAME =================
login_frame = tk.Frame(root, bg="#f4f6f7")
login_frame.pack(pady=100)

tk.Label(login_frame, text="Library System Login",
         font=("Arial", 18, "bold"),
         bg="#f4f6f7").pack(pady=10)

tk.Label(login_frame, text="Username:",
         bg="#f4f6f7").pack()

entry_username = tk.Entry(login_frame, width=30)
entry_username.pack(pady=5)

role_var = tk.StringVar(value="Student")

tk.Radiobutton(login_frame, text="Student",
               variable=role_var, value="Student",
               bg="#f4f6f7").pack()

tk.Radiobutton(login_frame, text="Admin",
               variable=role_var, value="Admin",
               bg="#f4f6f7").pack()

tk.Button(login_frame,
          text="Login",
          width=20,
          bg="#2e86c1",
          fg="white",
          command=login).pack(pady=15)

# ================= MAIN FRAME =================
main_frame = tk.Frame(root, bg="#f4f6f7")

# ----- Header -----
header_frame = tk.Frame(main_frame, bg="#d6eaf8")
header_frame.pack(fill="x")

user_label = tk.Label(header_frame,
                      text="",
                      font=("Arial", 12, "bold"),
                      bg="#d6eaf8")
user_label.pack(side="left", padx=10, pady=10)

total_label = tk.Label(header_frame,
                       text="Total Books: 0",
                       font=("Arial", 12),
                       bg="#d6eaf8")
total_label.pack(side="right", padx=10)

# ----- Book List -----
list_frame = tk.Frame(main_frame)
list_frame.pack(pady=15)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(list_frame,
                     width=70,
                     height=12,
                     yscrollcommand=scrollbar.set)
listbox.pack()

scrollbar.config(command=listbox.yview)

# ----- Buttons -----
button_frame = tk.Frame(main_frame, bg="#f4f6f7")
button_frame.pack(pady=10)

tk.Button(button_frame,
          text="Borrow",
          width=15,
          bg="#27ae60",
          fg="white",
          command=borrow_book).grid(row=0, column=0, padx=10)

tk.Button(button_frame,
          text="Return",
          width=15,
          bg="#e67e22",
          fg="white",
          command=return_book).grid(row=0, column=1, padx=10)

# ----- Add Book Section(Admin)-----
add_frame = tk.Frame(main_frame, bg="#f4f6f7")
add_frame.pack(pady=20)

tk.Label(add_frame,
         text="Add Book (Admin Only)",
         font=("Arial", 14, "bold"),
         bg="#f4f6f7").pack(pady=5)

entry_title = tk.Entry(add_frame, width=40)
entry_title.pack(pady=3)
entry_title.insert(0, "Title")

entry_author = tk.Entry(add_frame, width=40)
entry_author.pack(pady=3)
entry_author.insert(0, "Author")

entry_isbn = tk.Entry(add_frame, width=40)
entry_isbn.pack(pady=3)
entry_isbn.insert(0, "ISBN")

tk.Button(add_frame,
          text="Add Book",
          width=20,
          bg="#8e44ad",
          fg="white",
          command=add_book).pack(pady=10)

# =========================
# Start Application
# =========================
root.mainloop()