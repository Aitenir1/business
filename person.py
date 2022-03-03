import re
from constants import REGEX_EMAIL


class Person:

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password
        self.is_login = False

    @classmethod
    def validate_name(cls, name):
        if type(name) != str:
            raise Exception('Name must be a string type')

        if len(name) < 3:
            raise Exception('Name must contain at least 3 letters')

        if not name.isascii():
            raise Exception('Name must contain only ASCII letters')

        if name[0] != name[0].upper():
            raise Exception('Name must start with capital letter')

        for i in name:
            if i.isdigit():
                raise Exception('Name can not contain digits')

    @classmethod
    def validate_email(cls, email):
        if type(email) != str:
            raise Exception('Email must be a string type')

        if len(re.findall(REGEX_EMAIL, email)) == 0:
            raise Exception('Invalid email')

    @classmethod
    def validate_password(cls, password):
        if type(password) != str:
            raise Exception('Password must be a string type')

        if len(password) < 4:
            raise Exception('Password must contain at least 4 symbols')

        digits_count = 0

        for i in password:
            if i.isdigit():
                digits_count += 1

        if digits_count < 2:
            raise Exception('Add at least 2 letters to your password')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.validate_name(name)
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.validate_email(email)
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.validate_password(password)
        self.__password = password

    def log_in(self):
        self.is_login = True
