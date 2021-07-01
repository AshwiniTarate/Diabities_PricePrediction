from flask import Flask, request, jsonify
import test
import MongoDB
# import config

app = Flask(__name__)
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        data = request.form
        response = MongoDB.user_register(data)
    return jsonify({'msg':response})
    return data

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = request.form
        response = MongoDB.user_login(data)
    return jsonify({'msg':response})
    return data



@app.route('/predict_price', methods=['GET', 'POST'])
def predict_home_price():
    if request.method == 'POST':
        Pregnancies = (request.form['Pregnancies'])
        Glucose = int(request.form['Glucose'])
        BloodPressure = int(request.form['BloodPressure'])
        SkinThickness = int(request.form['SkinThickness'])
        Insulin = int(request.form['Insulin'])
        BMI = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = int(request.form['Age'])
        print('Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI, DiabetesPedigreeFunction,Age',Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI, DiabetesPedigreeFunction,Age)
        prediction = test.LogisticRegressionModel().outcome(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI, DiabetesPedigreeFunction,Age)
        MongoDB.saved_price_pred(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI, DiabetesPedigreeFunction,Age)

        return "The Predicted house price is Rs. {} lakhs".format(prediction)
    


if __name__ == "__main__":
    print("Starting Python Flask Server For Diabites Price Prediction...")
    # functions.load_saved_artifacts()
    app.run()