import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('JenisKelamin.sav', 'rb'))

st.title('Klasifikasi Gender')

long_hair = st.number_input('Panjang Rambut')
forehead_width_cm =st.number_input('Lebar Dahi (cm)')
forehead_height_cm = st.number_input('Panjang Dahi (cm)')
nose_wide = st.number_input('Hidung Lebar (1: Ya, 0: Tidak)')
nose_long =st.number_input('Hidung Panjang (1: Ya, 0: Tidak)')
lips_thin = st.number_input('Bibir Tipis (1: Ya, 0: Tidak)')
distance_nose_to_lip_long = st.number_input('Jarak Antara Hidung dan Bibir (1: Panjang, 0: Pendek)')

prediksi_gender = ''
if st.button('Hasil Prediksi'):
    prediksi_gender = model.predict([[long_hair, forehead_width_cm, forehead_height_cm, nose_wide, nose_long, lips_thin, distance_nose_to_lip_long]])
    
    if (prediksi_gender [0] == 0):
        prediksi_gender = 'Kamu Adalah Perempuan'
    else:
        prediksi_gender = 'Kamu Adalah Laki-laki'
st.success(prediksi_gender)