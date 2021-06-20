from .Person import Person


class Doctor(Person):
    __patient = __refId = None

    @classmethod
    def __init__(cls, name, email, refId, patient, password, has_license):
        super().__init__(name, email, password, has_license)
        cls.__refId = refId
        cls.__patient = patient

    # getters
    @property
    def refId(self):
        return self.__refId

    @property
    def patient(self):
        return self.__patient

    # setters
    @refId.setter
    def refId(self, new_refId):
        self.__refId = new_refId

    @patient.setter
    def patient(self, new_patient):
        self.__patient = new_patient

    def __repr__(self):
        return {"refID ": str(self.__refId),
                "doc_name": self.name,
                "doc_email": self.email,
                "patient": self.__patient}
