import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the model
try:
    model = pickle.load(open('model.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model file 'model.pkl' not found. Please ensure it is uploaded to the repository.")
    st.stop()

st.title("Anemia Prediction App")

st.write("Enter the following details to predict if you have anemia:")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"], key="gender")
hemoglobin = st.number_input("Hemoglobin (g/dL)", min_value=0.0, step=0.1, key="hemoglobin", help="Normal range: 12-16 g/dL for females, 14-18 g/dL for males")
mch = st.number_input("MCH (pg)", min_value=0.0, step=0.1, key="mch", help="Normal range: 27-32 pg")
mchc = st.number_input("MCHC (g/dL)", min_value=0.0, step=0.1, key="mchc", help="Normal range: 32-36 g/dL")
mcv = st.number_input("MCV (fL)", min_value=0.0, step=0.1, key="mcv", help="Normal range: 80-100 fL")

# Convert gender to numeric (assuming 0 for Male, 1 for Female)
gender_numeric = 0 if gender == "Male" else 1

if st.button("Predict"):
    features = np.array([[gender_numeric, hemoglobin, mch, mchc, mcv]])
    df = pd.DataFrame(features, columns=['Gender', 'Hemoglobin', 'MCH', 'MCHC', 'MCV'])
    
    prediction = model.predict(df)
    result = prediction[0]
    
    if result == 0:
        st.success("You don't have any Anemic Disease")
    elif result == 1:
        st.error("You have Anemic Disease")