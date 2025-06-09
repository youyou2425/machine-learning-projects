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

---

## 📁 How to Use the App

   Upload a CSV file with the exact columns listed above. The app will return a downloadable CSV with predictions and risk probabilities.

### 📥 Sample CSV File

You can download a sample input file to test batch prediction here:

👉 [Download sample_heart_risk_input.csv](https://github.com/youyou2425/machine-learning-projects/raw/main/streamlit_heart_app_updated/sample_heart_risk_input_numeric_country.csv)

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
