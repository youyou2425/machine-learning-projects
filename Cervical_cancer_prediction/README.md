# Cervical Cancer Prediction using XGBoost

## Project Overview
This project aims to predict **cervical cancer biopsy results** (0 = no cancer, 1 = cancer) based on patient data, including **age, smoking history, sexually transmitted diseases (STDs), and screening test results**. The goal is to develop a model that helps in early detection, reducing unnecessary procedures while minimizing missed diagnoses.

## Key Highlights
- **Best Model:** XGBoost with optimized precision and recall
- **Class imbalance handling:** Used combination of SMOTE_NC and scale_pos_weight in XGBoost to address class imbalance
- **Feature Importance:** Identified key risk factors using SHAP values
- **Threshold Tuning:** Improved model performance by selecting the best threshold (0.70)
- **Performance Metrics:** Achieved a balance between precision (0.65) and recall (1.0) on test data

## Repository Structure
```
📂 Cervical-Cancer-Prediction
│── 📄 README.md (This file)
│── 📂 data 
│── 📂 models 
│── 📂 results
│── 📄 Cervical_Cancer_Prediction_Using_XG_boost.ipynb (Colab notebook for EDA & model training)
```

## Results
| Metric  | Training | Testing  |
|---------|---------|----------|
| Precision | 0.69 | 0.67 |
| Recall | 0.89 | 0.75 |
| F1-score | 0.78 | 0.71 |

- **XGBoost outperformed other models** in balancing precision and recall.
- **SHAP analysis helped identify key features** contributing to cancer predictions.
- **Threshold tuning improved recall while maintaining precision.**

## Next Steps
- Experiment with **ensemble models**
- Explore **deep learning approaches** (e.g., Neural Networks)
- Integrate the model into a **web application** for clinicians

## Contact
For any questions, feel free to reach out!

---

🔗 **If you found this project useful, give it a ⭐ on GitHub!**

