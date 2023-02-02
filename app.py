import streamlit as st
import pandas as pd
import numpy as np
import pickle #to load a saved model

pickle_in = open('model_uas.pkl', 'rb')
nb = pickle.load(pickle_in)

def predict_charges(age, sex, bmi, children, smoker):
    charges = pickle.load(open('model_uas.pkl', 'rb'))
    return charges

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages

if app_mode=='Home':
    st.title('PREDIKSI ASURANSI :') 
    st.markdown('Rosita Milawati - 2019230038 - UAS Data Warehouse & Data Mining')
    st.image('insurance.jpg')
    st.title("Aplikasi untuk Prediksi Biaya Asuransi Kesehatan")
    st.markdown('Dataset :')
    data=pd.read_csv('insurance.csv')
    st.write(data.head())

elif app_mode == 'Prediction':
    st.image('prediction.png')
    st.write('\n')
    age = st.number_input("Age", min_value=1, max_value=100, value=30)
    sex = st.selectbox("Sex", ["1", "0"])
    bmi = st.number_input("BMI", min_value=10, max_value=40, value=25)
    children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
    smoker = st.selectbox("Smoker", ["1", "0"])
    charges =""
    
    if st.button("KLIK UNTUK PREDIKSI"):
        charges = predict_charges(age, sex, bmi, children, smoker)
    st.success("The charges are: {}".format(charges))
    
