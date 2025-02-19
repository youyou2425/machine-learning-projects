# Heart Attack Risk Prediction



## Project Overview

This project predicts the risk of a **heart attack** using machine learning. It analyzes various health indicators, such as cholesterol levels, blood pressure, age, and smoking habits, to identify high-risk individuals. The goal is to develop a model that can accurately identify high-risk individuals and support preventive healthcare by enabling early intervention.

## Key Highlights

- **Best Model:** Random Forest (selected for its high recall of 0.82)
- **Key Features:** Age, Blood Pressure, Cholesterol, Smoking, Diabetes, etc.
- **Evaluation Metrics:** Achieved high recall to prioritize identifying at-risk individuals
- **Feature Importance:** Visualized in results/Best\_model\_important\_features.txt

## Repository Structure

```
heart-attack-risk-prediction/
│── data/                  # Contains dataset (if public or sample available)
│── notebooks/             # Jupyter/Colab notebooks with analysis & modeling
│── models/                # Saved trained models (best_model.pkl)
│── results/               # Evaluation metrics, visualizations, and insights
│── README.md              # Project documentation
```

## Results

The best-performing model, **Random Forest**, achieved a recall of **0.82**, ensuring fewer false negatives in identifying high-risk individuals. Key evaluation metrics and visualizations are available in the `results/` folder.

## How to Use

If you want to explore the trained model:

```python
import joblib
model = joblib.load("models/best_model.pkl")
```

## Next Steps

- Further optimize hyperparameters for better precision-recall balance
- Explore deep learning approaches for improved prediction accuracy
- Expand feature engineering for more robust insights

## Contact

For any questions or discussions, feel free to reach out via GitHub.

---



