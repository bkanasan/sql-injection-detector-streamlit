import streamlit as st
import joblib

# Load model
model = joblib.load("sqli_detector.pkl")

st.title("SQL Injection Detector")
user_input = st.text_area("Enter a query to analyze:")

if st.button("Check"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        prediction = model.predict([user_input])[0]
        st.success(f"Prediction: {prediction}")
