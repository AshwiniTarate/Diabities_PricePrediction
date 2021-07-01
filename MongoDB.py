from pymongo import MongoClient
import MongoDB
import config

my_client = MongoClient(config.MONGODB_URL)
data_base = my_client[config.DPP_DATABASE]

# create columns in database
user_collection = data_base['user_details']
prediction_collection = data_base['prediction_details']

def user_register(user_data):
    user_details_dict = {}
    user_details_dict['username'] = user_data['username']
    user_details_dict['mailid'] = user_data['mailid']
    user_details_dict['mobile'] = user_data['mobile']
    user_details_dict['password'] = user_data['password']

    user_collection.insert_one(user_details_dict)
    return 'Successfully Registered'


def user_login(login_data):
    user_details_dict = {}
    user_details_dict['username'] = login_data['username']
    user_details_dict['password'] = login_data['password']

    result = user_collection.find_one(user_details_dict)
    if not result:
        return 'Invalid username or password'
        
    return 'Login Successful'

def saved_price_pred(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI, DiabetesPedigreeFunction,Age):
    price_details = {'Pregnancies' : Pregnancies, 'Glucose' : Glucose , 'BloodPressure' : BloodPressure , 'SkinThickness' : SkinThickness, 'Insulin' : Insulin, 'BMI' : BMI, 'Diabetes_Pedigree_Function' : DiabetesPedigreeFunction, 'Age' : Age}

    prediction_collection.insert_one(price_details)

    return 'Prediction Of Prices Successfully Saved ' 
