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

cont = st.container()
with cont:
    col1, col2, col3 = st.columns([1, 3, 1])
    image_file = col2.file_uploader("Upload your sample", type=["png", "jpg", "jpeg", "tif"])


def main():

    if image_file is not None:
        original_img = Image.open(image_file)
        image_data = np.asarray(original_img)

        blur, thresholding, filters = modification_bar()
        modified_img = show_modified_image(blur, thresholding, filters, image_data)

        #a, b = detect_ridges(modified_img, sigma=0.15)
        st.button(label='Extract Features')

        cont2 = st.container()
        col4, col5, col6 = cont2.columns(3)
        ''''
        m = col6.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: #00cc00;color:white;font-size:20px;height:3em;width:25em;border-radius:10px 10px 10px 10px;
        }
        </style>""", unsafe_allow_html=True)
        col6.button(label='Extract Features')
        '''

        with col4:
            st.markdown('Original Image')
            st.image(original_img)

        with col5:
            st.markdown('Modified Image')
            st.image(modified_img)

        with col6:
            st.markdown('Output Image')
            st.image(a, b)


if __name__ == '__main__':
    main()
