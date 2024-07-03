import pickle
import numpy as np
import streamlit as st

#load save model
model = pickle.load(open('penyakit_jantung.sav', 'rb'))

#judul web
st.title('PREDIKSI PENYAKIT JANTUNG')

col1, col2 = st.columns(2)

### coba running
with col1:
    male = st.number_input('Jenis Kelamin')
with col2:
    age = st.number_input('Umur')
with col1:
    CurrentSmoker = st.number_input('Status Merokok')
with col2:
    prevalentStroke = st.number_input('Riwayat Stroke')
with col1:
    prevalentHyp = st.number_input('Hopertensi')
with col2:
    diabetes = st.number_input('Diabetes')
with col1:
    totChol = st.number_input('Kolesterol')
with col2:
    heartRate = st.number_input('Denyut Jantung')
with col1:
    glucose = st.number_input('Kadar Gula Darah')

# code for prediction
heart_diagnosis =''

# membuat tombol prediksi
try:
    inputs = [float(male), float(age), float(CurrentSmoker), float(prevalentStroke), float(prevalentHyp), 
              float(diabetes), float(totChol), float(heartRate), float(glucose)]

    # Membuat tombol prediksi
    if st.button('Hasil Prediksi Penyakit Jantung'):
        heart_prediction = model.predict([inputs])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'Pasien Terkena Penyakit Jantung'
        else:
            heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'

    st.success(heart_diagnosis)

except ValueError:
    st.error('Please enter valid numeric values for all input fields.')