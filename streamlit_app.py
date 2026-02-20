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
hemoglobin = st.number_input("Hemoglobin", min_value=0.0, step=0.1, key="hemoglobin")
mch = st.number_input("MCH", min_value=0.0, step=0.1, key="mch")
mchc = st.number_input("MCHC", min_value=0.0, step=0.1, key="mchc")
mcv = st.number_input("MCV", min_value=0.0, step=0.1, key="mcv")

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