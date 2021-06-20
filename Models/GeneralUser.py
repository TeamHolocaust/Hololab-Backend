from Models.Person import Person


class GeneralUser(Person):
    # encapsulation
    __message = __name = __fbc = None

    @classmethod
    def __init__(cls, name, email, fbc, message, password, has_license):
        super().__init__(name, email, password, has_license)
        cls.__fbc = fbc
        cls.__message = message

    # getters
    @property
    def fbc(self):
        return self.__fbc

    @property
    def message(self):
        return self.__message

    # setters
    @fbc.setter
    def fbc(self, new_fbc):
        self.__fbc = new_fbc

    @message.setter
    def message(self, new_message):
        self.__message = new_message

    def __repr__(self):
        return {"name": self.name,
                "id": self.id,
                "fbc": self.__fbc,
                "prediction_message": self.__message}
