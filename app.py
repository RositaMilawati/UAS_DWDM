import streamlit as st
import pandas as pd
import numpy as np
import pickle #to load a saved model

pickle_in = open('model_uas.pkl', 'rb')
nb = pickle.load(pickle_in)

def prediction(age, sex, bmi, children, smoker):

    prediction = nb.predict([[age, sex, bmi, children, smoker]])
    print(prediction)
    return prediction

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages

if app_mode=='Home':
    st.title('Prediksi Biaya Asuransi Kesehatan :')
    st.image('prediction.png')
    st.title("Aplikasi Prediksi Pembayaran Asuransi Kesehatan Dengan Algoritma Regresi Linier")
    st.markdown('Dataset :')
    data=pd.read_csv('insurance1.csv')
    st.write(data.head())

elif app_mode == 'Prediction':
    st.image('prediction.png')
    st.write('\n')
    st.markdown('Masukkan informasi anda dibawah ini :')
    
    st.write('\n')
    age = st.number_input("Age", 0)
    sex = st.number_input("Sex", 0)
    bmi = st.number_input("BMI", 0)
    children = st.number_input("Children", 0)
    smoker = st.number_input("Smoker", 0)
    result =""
    
    if st.button("KLIK UNTUK PREDIKSI"):
        result = prediction(age, sex, bmi, children, smoker)
    st.success('Hasil Prediksi = {}'.format(result))
