from datamangment import DataManger
import os


class User:
    all_user = {}

    def __init__(self, username):
        self.username = username
        User.all_user[self.username] = self

    @classmethod
    def adding(cls, username):
        cls(username)

    @classmethod
    def deleting(cls, username):
        if username in cls.all_user.keys():
            del cls.all_user[username]

    def editing(self, new_username):
        self.username = new_username

    @classmethod
    def login(cls, username):
        if username in cls.all_user.keys():
            print(f"welcome {username}")
            return True

    def submit_login_user(self):
        with open("cache_logging.txt", "w") as file:
            file.write(self.username)

    @classmethod
    def check_cache(cls):
        if os.path.isfile("cache_logging.txt"):
            with open("cache_logging.txt", "r") as file:
                data = file.read()
                return cls.all_user[data]
        else:
            return None

