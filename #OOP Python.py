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
