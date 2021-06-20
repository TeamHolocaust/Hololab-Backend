from uuid import uuid4


class Person:
    # encapsulation
    __id = __name = __email = __has_license = __password = None

    @classmethod
    def __init__(cls, name, email, password, has_license):
        cls.__id = str(uuid4())
        cls.__name = name
        cls.__email = email
        cls.__has_license = has_license
        cls.__password = password

    # getters
    @property
    def email(self):
        return self.__email

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def has_license(self):
        return self.__has_license

    @property
    def password(self):
        return self.__password

    # setters
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @email.setter
    def email(self, new_email):
        self.__email = new_email

    @has_license.setter
    def has_license(self, new_license):
        self.__has_license = new_license

    def __repr__(self):
        return {'email': self.__email, "id": str(self.__id), "user_name": self.__name, "password": str(self.__password),
                'has_license': self.__has_license}
