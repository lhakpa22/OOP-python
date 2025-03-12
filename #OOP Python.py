# OOP Python
# User Class (Parent)
class User:
    def __init__(self, name, user_id, password, email):
        self.name = name
        self._user_id = user_id  # Protected attribute
        self.__password = password  # Private attribute
        self.email = email

    # getter for password
    def get_passwors(self):
        return self.__password

    # setter for password
    def set_password(self, new_password):
        self.__password = new_password
        print("password updated.")

    def login(self):
        print(f"{self.name} logged in.")

    def log_out(self):
        print(f"{self.name} logged out.")


# Member class (child of user)
class Member(User):
    def __init__(self, name, user_id, password, email, membership_type):
        super().__init__(name, user_id, password, email)
        self.membership_type = membership_type

    # Overriding the login method
    def login(self):
        print(
            f"{self.name} logged in as a Member with {self.membership_type} membership."
        )

    def borrow_book(self):
        print(f"{self.name} borrowed a book.")

    def return_book(self):
        print(f"{self.name}returned a book.")

    def reserve_book(self):
        print(f"{self.name}reserved a book.")

    def view_books(self):
        print(f"{self.name} is viewing book.")


# Librarian Class (Child of User)
class Librarian(User):
    def __init__(self, name, user_id, password, email, assigned_section):
        super().__init__(name, user_id, password, email)
        self.assigned_section = assigned_section

    def add_book(self):
        print(f"Librarian{self.name} addded a new book to the collection.")

    def remove_book(self):
        print(f"Librarian{self.name} removed a book from  the collection.")

    def issue_book(self):
        print(f"Librarian{self.name}issed  a book.")

    def overdue_report(self):
        print(f"Librarian{self.name}generate and overdue report")


# Admin class (child of user)
class Admin(User):
    def __init__(self, name, user_id, password, email, admin_level):
        super().__init__(name, user_id, password, email)

    def manage_users(self):
        print(f"Admin{self.name}is managing user")

    def set_library_rules(self, rule_name, rule_value):
        self.library_rules[rule_name] = rule_value
        print(f"Library Rule Updated: {rule_name} = {rule_value}")


# Book Class
class Book:
    def __init__(self, title, author, status="Available"):
        self.title = title
        self.author = author
        self.status = status

    def borrow_book(self):
        self.status = "Borrowed"
        print(f"The book '{self.title}' has been borrowed.")

    def return_book(self):
        self.status = "Available"
        print(f"The book '{self.title}' has been returned.")

    def reserve_book(self):
        self.status = "Reserved"
        print(f"The book '{self.title}' has been reserved.")

    def check_status(self):
        return self.status


# Library Class (Aggregation relation to book)
class Library:
    def __init__(self):
        self.books = []  # List to store Book objects
        self.users = []  # List to store User objects

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        print("Book not found.")
        return None

    def remove_book(self, title):
        book = self.search_book(title)
        if book:
            self.books.remove(book)
            print(f"Book '{title}' removed from the library.")

    def list_overdue(self):
        print("Listing overdue books...")
        for book in self.books:
            if book.check_status() == "Overdue":
                print(book.title)


# testing overriding
user1 = User("Amina", 225, "password123", "amina12@.com")
member1 = Member("will", 543, "password456", "will54@.com", "Premium")
