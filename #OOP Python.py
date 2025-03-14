# OOP Python
# User Class (Parent)
class User:
    def __init__(self, name, user_id, password, email):
        self.name = name
        self._user_id = user_id  # Protected attribute
        self.__password = password  # Private attribute
        self.email = email

    # getter for password
    def get_password(self):
        return self.__password

    # setter for password
    def set_password(self, new_password):
        self.__password = new_password
        print("password updated.")

    def login(self):
        print(f"{self.name} logged in.")

    def log_out(self):
        print(f"{self.name} logged out.")


# Member class (child of user) (intertance)
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


# Librarian Class (Child of User) (inheritance)
class Librarian(User):
    def __init__(self, name, user_id, password, email, assigned_section):
        super().__init__(name, user_id, password, email)
        self.assigned_section = assigned_section

    def add_book(self):
        print(f"Librarian {self.name} addded a new book to the collection.")

    def remove_book(self):
        print(f"Librarian {self.name} removed a book from  the collection.")

    def issue_book(self):
        print(f"Librarian {self.name} issed  a book.")

    def overdue_report(self):
        print(f"Librarian {self.name} generate and overdue report")


# Admin class (child of user) (inheritance)
class Admin(User):
    def __init__(self, name, user_id, password, email, admin_level):
        super().__init__(name, user_id, password, email)
        self.admin_level = admin_level
        self.library_rules = {}

    def manage_users(self):
        print(f"Admin {self.name} is managing user")

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


# Test Case 1: Testing the User class (Login and Logout )
user1 = User("Amina", 225, "password123", "amina12@.com")
user1.login()
user1.log_out()

# password update
print(f"old Password: {user1.get_password()}")
user1.set_password("newpassword456")
print(f"Updated Password: {user1.get_password()}")

# Test Case 2: Testing the Member class (Login with Membership and Borrow Book)
member1 = Member("will", 765, "password456", "will@.com", "Premium")
member1.login()
member1.borrow_book()

# Test Case 3: Testing the Librarian class (Add Book and Generate Report)
librarian1 = Librarian("Suneel", 101, "password789", "suneel@.com", "Fiction Section")
librarian1.add_book()
librarian1.overdue_report()

# Test Case 4: Testing the Admin class (Managing Users)
admin1 = Admin("lhakpa", 553, "adminpass", "Lhakpa@.com", "Super Admin")
admin1.manage_users()

admin1.set_library_rules("Max Borrow Limit", "5 books")
admin1.set_library_rules("Late Fee", "£3 per day")
print("Library Rules:", admin1.library_rules)

# Test Case 5: Testing the Book Class (Borrow, Return, and Check Status)
book1 = Book("A Little Life", "Hanya Yanagihara")
book1.borrow_book()
book1.return_book()
book1.reserve_book()
print(f"Book Status: {book1.check_status()}")

# Test Case 6: Testing the Library Class (Add, Search, Remove Book)
library = Library()
library.add_book(book1)
book2 = Book("Men Without Women", "Haruki Murakami")
library.add_book(book2)

# Search for a book
searched_book = library.search_book("A Little Life")
if searched_book:
    print(f"Found Book: {searched_book.title}")

# Remove a book
library.remove_book("Men Without Women")
