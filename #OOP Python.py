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

    def borrow_book(self):
        print(f"{self.name} borrowed a book")

    def return_book(self):
        print(f"{self.name}returned a book")
