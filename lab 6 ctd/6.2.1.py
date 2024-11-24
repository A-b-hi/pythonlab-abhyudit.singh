class PasswordManager:
    def __init__(self):
        self.__password = None  # Private member

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

pm = PasswordManager()
pm.set_password("my_secure_password")
print("Password set is:", pm.get_password())