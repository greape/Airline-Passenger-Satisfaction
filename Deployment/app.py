import pandas as pd 
import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox("choose page: ", ("Home page","Data exploration","Data Prediction"))

if page == "Home page":
    st.title("Plane Passanger Satisfaction Prediction")
    st.write("Name: Dicky Gabriel")
    st.write("Batch: SBY-002")
    st.write("Objective : Predict Plane Passanger Satisfaction")
elif page == "Data exploration":
    eda.run()
else:
    prediction.run()