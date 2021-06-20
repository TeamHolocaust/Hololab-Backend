class MedicalInformation:
    __age = __height = __weight = __gender = __systolic_blood_pressure = __diastolic_blood_pressure = __cholesterol = \
        __glucose = __smoking = __alcohol = __physical_activity = __severity = None

    @classmethod
    def __init__(cls, age, height, weight, gender, systolic_blood_pressure, diastolic_blood_pressure, cholesterol,
                 glucose, smoking, alcohol, physical_activity, severity):
        cls.age = age
        cls.__height = height
        cls.__weight = weight
        cls.__gender = gender
        cls.__systolic_blood_pressure = systolic_blood_pressure
        cls.__diastolic_blood_pressure = diastolic_blood_pressure
        cls.__cholesterol = cholesterol
        cls.__glucose = glucose
        cls.__smoking = smoking
        cls.__alcohol = alcohol
        cls.__physical_activity = physical_activity
        cls.__severity = severity

    # getter
    @property
    def age(self):
        return self.__age

    @property
    def height(self):
        return self.__height

    @property
    def weight(self):
        return self.__weight

    @property
    def gender(self):
        return self.__gender

    @property
    def systolic_blood_pressure(self):
        return self.__systolic_blood_pressure

    @property
    def diastolic_blood_pressure(self):
        return self.__diastolic_blood_pressure

    @property
    def cholesterol(self):
        return self.__cholesterol

    @property
    def glucose(self):
        return self.__glucose

    @property
    def smoking(self):
        return self.__smoking

    @property
    def alcohol(self):
        return self.__alcohol

    @property
    def physical_activity(self):
        return self.__physical_activity

    @property
    def severity(self):
        return self.__severity

    # setters
    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight

    @gender.setter
    def gender(self, new_gender):
        self.__gender = new_gender

    @systolic_blood_pressure.setter
    def systolic_blood_pressure(self, new_systolic_blood_pressure):
        self.__systolic_blood_pressure = new_systolic_blood_pressure

    @diastolic_blood_pressure.setter
    def diastolic_blood_pressure(self, new_diastolic_blood_pressure):
        self.__diastolic_blood_pressure = new_diastolic_blood_pressure

    @cholesterol.setter
    def cholesterol(self, new_cholesterol):
        self.__cholesterol = new_cholesterol

    @glucose.setter
    def glucose(self, new_glucose):
        self.glucose = new_glucose

    @smoking.setter
    def smoking(self, new_smoking):
        self.__smoking = new_smoking

    @alcohol.setter
    def alcohol(self, new_alcohol):
        self.__alcohol = new_alcohol

    @physical_activity.setter
    def physical_activity(self, new_physical_activity):
        self.__physical_activity = new_physical_activity

    @severity.setter
    def severity(self, new_severity):
        self.__severity = new_severity

    def __repr__(self):
        return {
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            "gender": self.gender,
            "systolic_blood_pressure": self.systolic_blood_pressure,
            "diastolic_blood_pressure": self.diastolic_blood_pressure,
            "cholesterol": self.cholesterol,
            "glucose": self.glucose,
            "smoking": self.smoking,
            "alcohol": self.alcohol,
            "physical_activity": self.physical_activity,
            "severity": self.severity
        }
