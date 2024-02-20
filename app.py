import streamlit as st
import warnings
import tensorflow as tf
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
import numpy as np
from keras.preprocessing import image
from PIL import ImageEnhance
from win32com.client import Dispatch

warnings.filterwarnings('ignore')


def speak(str1):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)


def main():
    st.title("PNEUMONIA Detection App")

    uploaded_file = st.file_uploader("Upload Chest X-ray Image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        model = load_model('pneumonia.h5')
        img = image.load_img(uploaded_file, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        img_data = preprocess_input(x)
        classes = model.predict(img_data)

        if classes[0][0] > 0.5:
            st.write("Result is Normal")
            speak("Result is Normal")
        else:
            st.write("Affected By PNEUMONIA")
            speak("Affected By PNEUMONIA")


if __name__ == '__main__':
    main()
