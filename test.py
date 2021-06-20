import unittest
from main import app
import json


class TestApi(unittest.TestCase):

    # before each test
    def setUp(self):
        self.test = app.test_client(self)

    # after each test
    def tearDown(self):
        print("Test successful")

    # home route
    def test_main(self):
        response_main = self.test.get("/")
        self.assertEqual(response_main.status_code, 200)

    # signup_doctor route
    def test_signup_doctor(self):
        credentials = json.dumps({
            "name": "TestDoctor",
            "email": "testdoctor@gmail.com",
            "referenceId": "1234567",
            "password": "12345678910",
            "cpassword": "12345678910"
        })
        response = self.test.post("/signup/doctor", headers={"Content-Type": "application/json"}, data=credentials)
        self.assertEqual(response.status_code, 201)    # checking status code
        self.assertTrue(b'message' in response.data)   # checking returned data

    # signup_normal_user route
    def test_signup_normal_user(self):
        credentials = json.dumps({
            "name": "TestPatient",
            "email": "testpatient@gmail.com",
            "password": "12345678910",
            "cpassword": "12345678910"
        })
        response = self.test.post("/signup/normalUser", headers={"Content-Type": "application/json"}, data=credentials)
        # self.assertEqual()
        self.assertEqual(response.status_code, 201)    # checking status code
        self.assertTrue(b'message' in response.data)   # checking returned data

    # login route
    # def test_login(self):
    #     credentials = json.dumps({
    #         "email": "testDoctor@gmail.com",
    #         "password": "12345678910"
    #     })
    #     response = self.test.post("/login", headers={"Content-Type": "application/json"}, data=credentials)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(b'message' in response.data)   # checking returned data
    #
    # prediction form route
    # def test_prediction_form(self):
    #     test_data = json.dumps({
    #         "name": "patient",
    #         "age": 50,
    #         "height": 168,
    #         "weight": 62,
    #         "gender": 2,
    #         "systolicBloodPressure": 110,
    #         "diastolicBloodPressure": 80,
    #         "cholesterol": 1,
    #         "glucose": 1,
    #         "smoking": 0,
    #         "alcohol": 0,
    #         "physicalActivity": 1
    #     })
    #     response = self.test.post("/predictionForm/testdoctor@gmail.com", headers={"Content-Type": "application/json"}, data=test_data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(b'message' in response.data)   # checking returned data
    #
    # # all details route
    # def test_allDeatails(self):
    #     response = self.test.get("allDetails/testdoctor@gmail.com")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(b'id' in response.data)   # checking id attribute in returned data
    #     self.assertTrue(b'name' in response.data)   # checking name attribute in returned data
    #
    # # patient route
    # def test_patient(self):
    #     response = self.test.get("patient/testdoctor@gmail.com/patient/results")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue(b'prediction_message' in response.data)


if __name__ == "__main__":
    unittest.main()
