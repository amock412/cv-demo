import streamlit as st
from utils import *
from PIL import Image

# Streamlit app
st.title('Object Detection')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file) # Use Image.open to open the image
    st.image(image, caption='Uploaded Image.', use_container_width=True) # use_column_width is optional, just helps for display
    st.write("")
    st.write("Detecting...")

    detected_image = detect_image(image)

    st.image(detected_image, caption='Detected Image.', use_container_width=True)