import streamlit as st
from PIL import Image
from modification import modification_bar, show_modified_image
import numpy as np
from ridge_detection import detect_ridges


@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img



st.set_page_config(layout="wide")

Form_button_html = """div.stButton > button:first-child {
background-color: #00cc00;color:white;font-size:20px;height:3em;width:30em;border-radius:10px 10px 10px 10px;"""


Title_html = """
        <style>
        
            #MainMenu {visibility: hidden; }
            footer {visibility: hidden; }
            header {visibility: hidden;}
            .title h1{
              user-select: none;
              font-size: 60px;
              color: white;
              text-align: center;
              background: repeating-linear-gradient(-45deg, red 0%, yellow 7.14%, rgb(0,255,0) 14.28%, rgb(0,255,255) 21.4%, cyan 28.56%, blue 35.7%, magenta 42.84%, red 50%);
              background-size: 600vw 600vw;
              -webkit-text-fill-color: transparent;
              -webkit-background-clip: text;
              animation: slide 10s linear infinite forwards;
            }
            @keyframes slide {
              0%{
                background-position-x: 0%;
              }
              100%{
                background-position-x: 600vw;
              }
            }
        </style> 

        <div class="title">
            <h1>Fingerprint Feature Extraction</h1>
        </div>
        """
st.markdown(Title_html, unsafe_allow_html=True)

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

        with col10:
            st.button("Extract features")


if __name__ == '__main__':
    main()
