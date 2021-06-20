from flask import Flask, request, jsonify
from flask_cors import CORS
import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore
from werkzeug.security import generate_password_hash

# to load the Machine Learning Model importing the Modules
from tensorflow import keras
from tensorflow.keras.models import load_model

# import the Models
from Models.Person import Person
from Models.GeneralUser import GeneralUser
from Models.Patient import Patient
from Models.MedicalInformation import MedicalInformation
from Models.Doctor import Doctor

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdgp-holocaust-alter-project'  # database secret key
cors = CORS(app, resources={r"/*": {"origins": "*"}})  # enabling CORS

# connecting to firebase
cred = credentials.Certificate("ServiceKey/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
databaseConnection = firestore.client()
main_collection_database = databaseConnection.collection("users")  # main collection of the database

firebaseConfig = {
    "apiKey": "AIzaSyAd2XajThp4HvutLUBvcT9LkkiLEEY7vMw",
    "authDomain": "hololab-9b8cc.firebaseapp.com",
    "databaseURL": "https://hololab-9b8cc-default-rtdb.firebaseio.com",
    "projectId": "hololab-9b8cc",
    "storageBucket": "hololab-9b8cc.appspot.com",
    "messagingSenderId": "968649685164",
    "appId": "1:968649685164:web:e9045f1e64fae445f88709",
}

firebase = pyrebase.initialize_app(firebaseConfig)  # Connecting to the Firebase
authenticating = firebase.auth()  # making the authenticating process


# loading the model
def get_model():
    global model
    model = load_model("Machine_Learning_Model/prediction_model.h5")
    print(" * Model Loaded!!")


print(" * Loading Keras Model ")
get_model()


@app.route('/')
def hello_world():
    return 'Hello World starting!'


@app.route('/signup/normalUser', methods=['POST'])
def signup_normal_user():
    if request.is_json:
        name = request.json['name']
        email_normal_user = request.json['email']
        password_normal_user = request.json['password']
        confirm_password_normal_user = request.json['cpassword']

    else:
        name = request.form['name']
        email_normal_user = request.form['email']
        password_normal_user = request.form['password']
        confirm_password_normal_user = request.form['cpassword']

    # checking if the password and the confirm password matches
    if password_normal_user == confirm_password_normal_user:
        if request.method == 'POST':

            try:
                # checking if the user can sign in
                # checking if the user already exist
                # creating the user
                authenticating.create_user_with_email_and_password(email=email_normal_user,
                                                                   password=password_normal_user)

                # instantiating Person class
                normal_person_details = Person(name=name, email=email_normal_user,
                                               password=generate_password_hash(password_normal_user, 'sha256'),
                                               has_license=False)
                # adding to the database
                main_collection_database.document(email_normal_user).set(normal_person_details.__repr__())

                # when user successfully created
                return jsonify(message="Successfully signed up"), 201

            except:
                # when the user already exist
                return jsonify(message="User Already Exist")

    # when the passwords do not match
    return jsonify(message='Sorry the password doesnt Match')


@app.route('/signup/doctor', methods=['POST'])
def signup_doctor():
    if request.is_json:
        doctor_name = request.json['name']
        email_doctor = request.json['email']
        reference = request.json['referenceId']
        password_doctor = request.json['password']
        confirm_password_doctor = request.json['cpassword']

    else:
        doctor_name = request.form['name']
        email_doctor = request.form['email']
        reference = request.form['referenceId']
        password_doctor = request.form['password']
        confirm_password_doctor = request.form['cpassword']

    # checking whether two passwords match
    if password_doctor == confirm_password_doctor:
        if request.method == 'POST':

            try:
                # creating the user with email and password
                authenticating.create_user_with_email_and_password(email=email_doctor, password=password_doctor)

                # instantiating the Person class
                doctor_registration = Person(name=doctor_name, email=email_doctor,
                                             password=generate_password_hash(password_doctor, 'sha256'),
                                             has_license=True)

                # adding data to the database
                doctor_details = {'reference-id': str(reference)}
                main_collection_database.document(email_doctor).set(doctor_registration.__repr__())
                main_collection_database.document(email_doctor).set(doctor_details, merge=True)

                # when the doctor is successfully signed up
                return jsonify(message='Successfully made a doctor signup'), 201

            except:
                # when the doctor already exist
                return jsonify(message='Doctor Already Exist Please Login or sign up')

    # when the passwords do not match
    return jsonify(message='The Password doesnt Match')


@app.route("/predictionForm/<string:email_id>", methods=['POST'])
def prediction_form(email_id):
    if request.method == 'POST':
        patient_name = request.json['name']
        age = request.json['age']
        height = request.json['height']
        weight = request.json['weight']
        gender = request.json['gender']
        systolic_blood_pressure = request.json['systolicBloodPressure']
        diastolic_blood_pressure = request.json['diastolicBloodPressure']
        cholesterol = request.json['cholesterol']
        glucose = request.json['glucose']
        smoking = request.json['smoking']
        alcohol = request.json['alcohol']
        physical_activity = request.json['physicalActivity']

        # checking the range of glucose and cholesterol

        # cholesterol
        cholesterol_well_above_normal = False
        cholesterol_above_normal = False
        cholesterol_normal = False
        if float(cholesterol) < 200:
            cholesterol_normal = True
            cholesterol_message = "Normal"
        elif float(cholesterol) < 240:
            cholesterol_above_normal = True
            cholesterol_message = "Above normal"
        else:
            cholesterol_well_above_normal = True
            cholesterol_message = "Well above normal"

        # glucose
        glucose_well_above_normal = False
        glucose_above_normal = False
        glucose_normal = False
        if float(glucose) < 108:
            glucose_normal = True
            glucose_message = "Normal"
        elif float(glucose) < 180:
            glucose_above_normal = True
            glucose_message = "Above normal"
        else:
            glucose_well_above_normal = True
            glucose_message = "Well above normal"

        # checking the gender
        is_female = False
        is_male = False
        if gender == "1":
            is_female = True
        else:
            is_male = True

        # Checking the Systolic Blood Pressure
        if float(systolic_blood_pressure) > 129:
            systolic_blood_pressure_message = "High blood pressure"
        else:
            systolic_blood_pressure_message = "Normal"

        # Checking the Diastolic Blood Pressure
        if float(diastolic_blood_pressure) > 80:
            diastolic_blood_pressure_message = "High blood pressure"
        else:
            diastolic_blood_pressure_message = "Normal"

        # converting height to meters
        # from the user height is taken in cm
        # convert height into meters feed to the model
        height_in_meters = float(height) / 100

        # calculate BMI
        bmi = float(weight) / (height_in_meters * height_in_meters)

        # feeding the model with data
        prediction = model.predict([[float(age), float(height), float(weight),
                                     float(systolic_blood_pressure), float(diastolic_blood_pressure),
                                     float(smoking), float(alcohol), float(physical_activity), float(bmi),
                                     cholesterol_above_normal, cholesterol_normal, cholesterol_well_above_normal,
                                     glucose_above_normal, glucose_normal, glucose_well_above_normal,
                                     is_female, is_male]])

        # Converting the numeric values to meaningful phrases
        # those messages will be displayed to the user and will be stored in database
        message_yes = "Yes"
        message_no = "No"

        # gender
        if gender == "1":
            gender = "Female"
        else:
            gender = "Male"

        # smoking
        if smoking == "1":
            smoking = message_yes
        else:
            smoking = message_no

        # alcohol
        if alcohol == '1':
            alcohol = message_yes
        else:
            alcohol = message_no

        # physical activities
        if physical_activity == "1":
            physical_activity = message_yes
        else:
            physical_activity = message_no

        # streaming through the collection by email
        check_license = main_collection_database.where('email', '==', email_id).stream()
        model_message = ""  # this will help to store the Value of the User

        for doc in check_license:
            # checking if the user is a doctor or not
            if doc.get('has_license'):

                # checking prediction result and sending result details accordingly
                if prediction > 0.5:
                    # result to be displayed to the user
                    model_message = {"predictionMessage": "The patient has a possibility of cardiovascular disease.",
                                     "severity": str(round((prediction[0][0] * 100), 2)) + " % ",
                                     "cholesterol": cholesterol_message, "glucose": glucose_message,
                                     "systolic": systolic_blood_pressure_message,
                                     "diastolic": diastolic_blood_pressure_message}
                else:
                    model_message = {"predictionMessage": "The patient does not have a cardiovascular disease.",
                                     "severity": str(round((prediction[0][0] * 100), 2)) + " % ",
                                     "cholesterol": cholesterol_message, "glucose": glucose_message,
                                     "systolic": systolic_blood_pressure_message,
                                     "diastolic": diastolic_blood_pressure_message}

                # instantiating MedicalInformation class
                medical_information_values = MedicalInformation(age, height, weight, gender, systolic_blood_pressure,
                                                                diastolic_blood_pressure, cholesterol, glucose, smoking,
                                                                alcohol,
                                                                physical_activity, model_message.get("severity"))

                # instantiating Patient class
                patient_details = Patient(patient_name, medical_information_values.__repr__(),
                                          model_message.get("predictionMessage"))

                # adding data to the collection in database
                main_collection_database.document(email_id).collection(patient_name).document().set(
                    patient_details.__repr__(), merge=True)

                # returning the model message to be displayed to the user
                doctor_message_array = [model_message]
                return jsonify(doctor_message_array)

            # if the user is a normal user
            else:
                if prediction > 0.5:
                    model_message = {"predictionMessage": "Very high risk of getting a cardiovascular disease.",
                                     "severity": "Please seek medical advices immediately .",
                                     "cholesterol": cholesterol_message, "glucose": glucose_message,
                                     "systolic": systolic_blood_pressure_message,
                                     "diastolic": diastolic_blood_pressure_message}
                elif prediction > 0.3:
                    model_message = {"predictionMessage": "High risk of getting a cardiovascular disease.",
                                     "severity": "Please contact a doctor.", "cholesterol": cholesterol_message,
                                     "glucose": glucose_message, "systolic": systolic_blood_pressure_message,
                                     "diastolic": diastolic_blood_pressure_message}
                else:
                    model_message = {"predictionMessage": "No risk of getting a cardiovascular disease.",
                                     "severity": "Continue a healthy lifestyle.", "cholesterol": cholesterol_message,
                                     "glucose": glucose_message,"systolic": systolic_blood_pressure_message,
                                     "diastolic": diastolic_blood_pressure_message}

                # instantiating MedicalInformation class
                medical_information_values = MedicalInformation(age, height, weight, gender, systolic_blood_pressure,
                                                                diastolic_blood_pressure, cholesterol, glucose, smoking,
                                                                alcohol,
                                                                physical_activity, model_message.get("severity"))

                # instantiating GeneralUser class
                normal_user_details = GeneralUser(patient_name, email_id, medical_information_values.__repr__(),
                                                  model_message.get("predictionMessage"), '****', False)

                # adding data to the database
                main_collection_database.document(email_id).collection(patient_name).document().set(
                    normal_user_details.__repr__(), merge=True)

                # returning the model message
                normal_user_message_array = [model_message]
                return jsonify(normal_user_message_array)
    return jsonify(message='Done')


@app.route('/allDetails/<string:email_id>')
def details_view(email_id):
    # retrieving the collection of a specific email id
    collections = main_collection_database.document(email_id).collections()

    # a list containing all the data of a specific email id
    all_details = []

    # traversing through the collection
    for collection in collections:
        # retrieving data from the collection
        for doc in collection.stream():
            # appending data to the list
            all_details.append(doc.to_dict())

    # a list containing unique names
    sample_send = []

    # looping to get the unique values
    values = {value['name']: value for value in all_details}.values()

    for val in values:
        # getting the name and ID of the Patient
        patient_id = {'id': val['id'], 'name': val['name']}
        sample_send.append(patient_id)

    # returning unique names
    return jsonify(sample_send)


@app.route('/patient/<string:email_id>/<string:patient_name>/results')
def show_specific_details(email_id, patient_name):
    # retrieving data specific to a patient name
    each_person_fbc = main_collection_database.document(email_id).collection(patient_name).where("name", "==",
                                                                                                 patient_name).stream()
    sample = []
    for doc in each_person_fbc:
        sample.append(doc.to_dict())
    return jsonify(sample)


if __name__ == '__main__':
    app.run()
