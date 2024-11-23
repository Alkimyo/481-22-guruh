import streamlit as st
import joblib

# Modelni yuklash
file_path_joblib = '/home/shohruh/Downloads/fitted_model.joblib'

try:
    model = joblib.load(file_path_joblib)
except Exception as e:
    st.error(f"Modelni yuklashda xatolik yuz berdi: {e}")
    st.stop()

st.set_page_config(page_title="Diabetes Bashorat Dasturi", page_icon="🩺", layout="centered")
st.title("Diabetes Bashorat Dasturi")

age = st.number_input("Yosh", min_value=0, max_value=120, step=1)
sex = st.selectbox("Jins", ["Erkak", "Ayol"])
bp = st.number_input("Qon bosimi (Blood Pressure)", min_value=0, max_value=200, step=1)
cholesterol = st.selectbox("Xolesterol", ["Normal", "Yuqori"])
na_to_k = st.number_input("Na to K darajasi", min_value=0.0, max_value=20.0, step=0.1)

# Tanlovlarni model uchun mos qiymatga aylantirish
sex_value = 0 if sex == "Ayol" else 1
cholesterol_value = 0 if cholesterol == "Normal" else 1

# Natijani hisoblash
if st.button("Hisoblash"):
    input_data = [[age, sex_value, bp, cholesterol_value, na_to_k]]
    
    try:
        prediction = model.predict(input_data)
        
        # Bashorat natijasini olish
        if isinstance(prediction[0], (int, float)):
            predicted_class_index = int(prediction[0])
        else:
            predicted_class_index = 0  # Default

        # Sinf nomlarini xaritaga solish
        class_mapping = {0: 'DA0', 1: 'DA1', 2: 'DA2', 3: 'DA3', 4: 'DA4'}
        
        # Bashorat qilingan sinf nomini olish
        predicted_class = class_mapping.get(predicted_class_index, 'Noma' )  # Default 'Noma' for invalid predictions

        st.success(f"Bashorat: {predicted_class}")
    except Exception as e:
        st.error(f"Bashorat qilishda xatolik: {e}")
