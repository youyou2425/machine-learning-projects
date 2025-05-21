from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

#Initialize Flask app instance. __name__tells Flask where to look for resources
app = Flask(__name__)

# Load the model
model = joblib.load("heart_attack_risk_best_model.pkl")

#Defines a home route (/) of your web API
@app.route('/')

#When someone goes to your app’s root URL, this function runs and returns a simple status message
def index():
    return "Heart Attack Risk Prediction API is running!"

#Defines the **`/predict` endpoint**, which only accepts **POST** requests
#When someone sends a POST request to the /predict URL, call the predict() function
#POST is a HTTP method to submit data (send input to the server) in web applications and APIs
#With POST, you can send a JSON payload (your model’s input features)
#This is the route users will call to get a prediction
@app.route('/predict', methods=['POST'])

#accept input with named fields like this:
##{
##  "age": 57,
##  "sex": 1,
##  "cp": 0,
##  "trestbps": 140,
##  "chol": 241,
##  "fbs": 0,
##  "restecg": 0,
##  "thalach": 123,
##  "exang": 1,
##  "oldpeak": 0.2,
##  "slope": 1,
##  "ca": 0,
##  "thal": 3
##}

def predict():
    #Gets the JSON input sent in the POST request
    data = request.get_json()

    #fields required for the model to run
    required_fields = ['Age', 'Cholesterol', 'Heart Rate', 'Diabetes', 'Family History',
       'Obesity', 'Alcohol Consumption', 'Exercise Hours Per Week',
       'Previous Heart Problems', 'Medication Use', 'Stress Level',
       'Sedentary Hours Per Day', 'Income', 'BMI', 'Triglycerides',
       'Physical Activity Days Per Week', 'Sleep Hours Per Day', 'Country',
       'Systolic', 'Diastolic', 'Diet_1', 'Diet_2', 'Smoking']

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing one or more required input fields"}), 400

    features = [data[field] for field in required_fields]

    #Uses the model to predict the class (e.g., 1 = high risk, 0 = low risk)
    #The `[features]` wraps the list into a 2D array (shape `[1, n_features]`) which is required by scikit-learn models
    #`[0]` gets the first prediction result
    prediction = model.predict([features])[0]

    #Gets the probability the model assigns to the positive class (heart attack risk)
    #predict_proba returns [ [prob_class_0, prob_class_1] ]; the [1] pulls out the probability of class 1    
    proba = model.predict_proba([features])[0][1]

    #Sends the model’s results back as JSON
    #`prediction`: 0 or 1 (e.g., no risk vs. high risk)
    #`risk_probability`: the model’s confidence (rounded to 4 decimal places)
    return jsonify({
        "prediction": int(prediction),
        "risk_probability": round(proba, 4)
    })

#This is the route users will call to get a prediction when input data is a csv file
@app.route('/predict_csv', methods=['POST'])

#accept input csv file like this:
##age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
##57,1,0,140,241,0,0,123,1,0.2,1,0,3
##62,0,2,130,270,1,1,150,0,1.0,2,1,2

def predict_csv():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        df = pd.read_csv(file)

        required_columns = ['Age', 'Cholesterol', 'Heart Rate', 'Diabetes', 'Family History',
       'Obesity', 'Alcohol Consumption', 'Exercise Hours Per Week',
       'Previous Heart Problems', 'Medication Use', 'Stress Level',
       'Sedentary Hours Per Day', 'Income', 'BMI', 'Triglycerides',
       'Physical Activity Days Per Week', 'Sleep Hours Per Day', 'Country',
       'Systolic', 'Diastolic', 'Diet_1', 'Diet_2', 'Smoking']

        if not all(col in df.columns for col in required_columns):
            return jsonify({"error": "Missing required columns"}), 400

        X = df[required_columns]
        preds = model.predict(X)
        probas = model.predict_proba(X)

        df['prediction'] = preds
        df['risk_probability'] = probas[:, 1].round(4)

        results = df.to_dict(orient='records')
        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
