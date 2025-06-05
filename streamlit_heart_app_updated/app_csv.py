
import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model and scaler
model = joblib.load("heart_attack_risk_best_model.pkl")
scaler = joblib.load("heart_attack_risk_scaler.pkl")
feature_columns = joblib.load("heart_attack_risk_feature_columns.pkl")

st.title("Heart Attack Risk Predictor")
st.write("Use this tool to predict heart attack risk by uploading a CSV file for batch prediction.")

# CSV Upload Section
st.header("📄 Batch Prediction via CSV Upload")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        # Retrict input to feature_columns
        df = df[feature_columns]
        
        if not all(col in df.columns for col in feature_columns):
            st.error("Missing one or more required columns in uploaded CSV.")
        else:
            scaled_batch = scaler.transform(df)
            # Wraps scaled input in a DataFrame with correct column names before prediction
            scaled_df = pd.DataFrame(scaled_batch, columns=feature_columns)

            probas = model.predict_proba(scaled_df)[:, 1]  # probability of class 1
            df["Risk Probability"] = probas.round(4)
            threshold = 0.35
            df["Prediction"] = (probas >= threshold).astype(int)
            
            st.success("Batch prediction complete.")
            
            st.dataframe(df)
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Results as CSV", data=csv, file_name="heart_attack_predictions.csv", mime='text/csv')

    except Exception as e:
        st.error(f"An error occurred: {e}")
