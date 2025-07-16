'''
How to run this locally?

In your terminal, use the command:
python -m streamlit run app.py
'''

import joblib
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import tensorflow as tf


@st.cache_resource
def load_model(model_path=None):
    if model_path is not None:
        return tf.keras.models.load_model(model_path)
    else:
        print("Model tidak ditemukan")
        return None
    

if __name__ == "__main__":

    model = load_model(model_path='bone_fracture_model.h5')
    class_names = ['Fractured', 'Not Fractured'] 

    st.title("🦴 Bone Fracture Classifier")
    st.write("Upload X-ray image untuk memprediksi apakah fractured atau tidak.")

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:

        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption="Upload Gambar", use_column_width=True)

        img = image.resize((180, 180))  
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)[0][0]  
        class_pred = class_names[int(prediction > 0.5)]
        confidence = prediction if prediction > 0.5 else 1 - prediction

        st.subheader("Hasil Prediksi:")
        st.write(f"**Class:** {class_pred}")
        st.write(f"**Confidence:** {confidence*100:.2f}%")
