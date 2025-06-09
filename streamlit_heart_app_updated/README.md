# 🫀 Heart Attack Risk Prediction App

This interactive Streamlit web app uses a machine learning model to predict an individual's risk of heart attack based on commonly collected health and lifestyle factors. It supports batch predictions via CSV upload.

![screenshot](https://github.com/youyou2425/machine-learning-projects/blob/main/streamlit_heart_app_updated/screenshot_heart_app.png?raw=true)

## 🚀 Live Demo

👉 [Click here to use the app][https://machine-learning-projects-ajonljppcjg3mlz3ehguyq.streamlit.app/]

---

## 💡 How It Works

- Trained a machine learning model (Random Forest) on synthetic clinical data
- Applied **MinMaxScaler** to standardize features
- Tuned prediction threshold to improve recall for early detection
- Deployed using **Streamlit Cloud**

---

## 📊 Input Features

The app expects the following 23 features for each prediction:

- Age, Cholesterol, Heart Rate, Diabetes, Family History, Obesity, Alcohol Consumption, Exercise Hours Per Week, Previous Heart Problems, Medication Use, Stress Level, Sedentary Hours Per Day, Income, BMI, Triglycerides, Physical Activity Days Per Week, Sleep Hours Per Day, Country (numeric), Systolic, Diastolic, Diet_1, Diet_2, Smoking

### Input Feature Ranges, Accepted Formats & Notes
Feature	Type	Range / Values	Format	Notes
Age	Numeric	18 – 90	Integer	Age in years
Cholesterol	Numeric	120 – 400	Integer	Blood cholesterol in mg/dL
Heart Rate	Numeric	40 – 110	Integer	Heartbeats per minute
Diabetes	Binary	0 = No, 1 = Yes	Integer	History of diabetes
Family History	Binary	0 = No, 1 = Yes	Integer	Family history of heart disease
Obesity	Binary	0 = No, 1 = Yes	Integer	Based on BMI or clinical diagnosis
Alcohol Consumption	Binary	0 = No, 1 = Yes	Integer	Consumes alcohol regularly
Exercise Hours Per Week	Numeric	0.00 – 20.00	Float	Weekly exercise in hours
Previous Heart Problems	Binary	0 = No, 1 = Yes	Integer	History of any heart-related diagnosis
Medication Use	Binary	0 = No, 1 = Yes	Integer	Currently on medication for heart-related issues
Stress Level	Numeric	1.00 – 10.00	Float	Self-reported on a scale from 1 (low) to 10 (high)
Sedentary Hours Per Day	Numeric	0.00 – 11.99	Float	Average daily sedentary time in hours
Income	Numeric	20,140 – 299,954	Integer	Annual household income in USD
BMI	Numeric	18.00 – 40.00	Float	Body Mass Index (weight/height²)
Triglycerides	Numeric	30 – 800	Integer	Triglyceride level in mg/dL
Physical Activity Days Per Week	Numeric	0 – 7	Integer	Number of days with moderate activity
Sleep Hours Per Day	Numeric	4.00 – 10.00	Float	Average hours of sleep per day
Systolic	Numeric	90 – 180	Integer	Systolic blood pressure (mm Hg)
Diastolic	Numeric	60 – 110	Integer	Diastolic blood pressure (mm Hg)
Diet_1	Binary	0 = Not Healthy, 1 = Healthy	Integer	Dummy variable from 3-class diet field
Diet_2	Binary	0 = Not Unhealthy, 1 = Unhealthy	Integer	Dummy variable from 3-class diet field
Smoking	Binary	0 = No, 1 = Yes	Integer	Current or past smoker
---

## 📁 How to Use the App

   Upload a CSV file with the exact columns listed above. The app will return a downloadable CSV with predictions and risk probabilities.

### 📥 Sample CSV File

You can download a sample input file to test batch prediction here:

👉 [Download sample_heart_risk_input.csv](https://drive.google.com/uc?export=download&id=1fOpmRQiS-BpipNMx2pJ3vl4-89QBySWB)

---

## 🧠 Model Details

- Model type: `RandomForestClassifier`
- Evaluation metric: prioritized **recall**
- Custom prediction threshold: `0.35`
- Built using `scikit-learn`, `pandas`, `numpy`, `joblib`, and `Streamlit`

---

## 🛠 How to Run Locally

```bash
git clone https://github.com/youyou2425/machine-learning-projects.git
cd machine-learning-projects/streamlit_heart_app_updated
pip install -r requirements.txt
streamlit run app_csv.py
