from uuid import uuid4


class Patient:

    # encapsulation
    __fbc = __predictResult = __name = __id = None

    @classmethod
    def __init__(cls, name, fbc, predictResult):
        cls.__id = str(uuid4())
        cls.__name = name
        cls.__fbc = fbc
        cls.__predictResult = predictResult

    # getters
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def predictionResult(self):
        return self.__predictResult

    @property
    def fbc(self):
        return self.__fbc

    # setters
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @predictionResult.setter
    def predictionResult(self, new_result):
        self.__predictResult = new_result

    @fbc.setter
    def fbc(self, new_fbc):
        self.__fbc = new_fbc

    def __repr__(self):
        return {"id": str(self.__id),
                "name": str(self.__name),
                "fbc": self.__fbc,
                "prediction_message": str(self.__predictResult)
                }
