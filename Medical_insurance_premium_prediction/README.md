# Medical Insurance Premium Prediction

## Project Overview

This project predicts medical insurance costs based on various factors such as age, BMI, smoking status, and region. The goal is to develop a machine learning model that provides accurate estimates of insurance premiums, which can help insurance companies, healthcare providers, and individuals make informed financial decisions.

## Problem Statement

Medical insurance premiums vary depending on multiple personal and lifestyle factors. This project aims to build a regression model that can estimate insurance charges based on input features such as age, BMI, smoker status, and region.

## Dataset

- **Source:** The dataset used in this project is the *Medical Cost Personal Dataset* from Kaggle.
- **Features:**
  - `age`: Age of the individual
  - `sex`: Gender of the individual
  - `bmi`: Body Mass Index
  - `children`: Number of dependent children
  - `smoker`: Smoking status (Yes/No)
  - `region`: Residential region
  - `charges`: Medical insurance cost (Target variable)

## Tech Stack

- **Programming Language:** Python
- **Libraries Used:** Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn, TensorFlow/Keras&#x20;
- **Machine Learning Models:**  Artificial Neural Networks (ANN)

## Model Development

1. **Exploratory Data Analysis (EDA)**

   - Data cleaning and preprocessing
   - Visualizing relationships between variables
   - Checking for missing values and outliers

2. **Feature Engineering**

   - Encoding categorical variables (e.g., `sex`, `smoker`, `region`)
   - Scaling numerical features&#x20;

3. **Model Training and Evaluation**

   - Implemented multiple neural network models&#x20;
   - Evaluated performance using training and validation loss plot, and metrics such as R², RMSE, and MAE 
   - Used **Early Stopping** and **Dropout** in ANN to prevent overfitting

## Results

- **Best Model:** neural network
- **R² Score:** 0.86 (example)
- **Key Insights:** Smoking status has the highest impact on insurance charges, followed by BMI and age.

## Repository Structure

```
├── data/                 # Raw and processed datasets
├── Medical_Insurance_Premium_Prediction_with_neural_network.ipynb  # Google Colab notebook for EDA and model            training
├── models/               # Saved machine learning models
├── results/              # Performance metrics and visualizations
├── README.md             # Project documentation

```


## Future Improvements

- Incorporate more features such as pre-existing medical conditions
- Experiment with tree models


## License

This project is licensed under the MIT License.

---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/youyou2425/machine-learning-projects/refs/heads/main/Medical_insurance_premium_prediction/Medical_Insurance_Premium_Prediction_with_Machine_Learning.ipynb)


