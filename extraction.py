import streamlit as st
from PIL import Image
from modification import *
import numpy as np
from ridge_detection import detect_ridges


@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img

st.set_page_config(layout="wide")

Title_html = open("index.html", 'r', encoding='utf-8')
source_code = Title_html.read()
st.markdown(source_code, unsafe_allow_html=True)

col1, col2, col3 = st.columns([3, 6, 3])
image_file = col2.file_uploader("Upload your fingerprint", type=["png", "jpg", "jpeg", "tif"])
col4, col5, col6, col7 = st.columns([3, 4.5, 1.5, 3])
col8, col9, col10, col11, col12, col13 = st.columns([3, 1.5, 1.5, 1.5, 1.5, 3])


def main():

    if image_file is not None:
        original_img = Image.open(image_file)
        image_data = np.asarray(original_img)

        with col5:
            st.markdown('Original Image')
            st.image(original_img, use_column_width=True)

        with col6:
            st.markdown('Modify Image')
            blur, tresholding, filters = modification_bar()
            st.button('Apply modifications')
            apply_blur(blur, image_data)

        with col10:
            st.button("Extract features")


if __name__ == '__main__':
    main()
