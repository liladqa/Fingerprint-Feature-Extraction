import streamlit as st
from PIL import Image

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
    image_file = col2.file_uploader("Upload your sample", type=["png", "jpg", "jpeg"])

cont2 = st.container()

def main():

    if image_file is not None:
        col4, col5, col6, col7, col8 = cont2.columns([1, 1, 1, 1, 1])
        col6.image(load_image(image_file), width=400)
        m = col6.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: #00cc00;color:white;font-size:20px;height:3em;width:25em;border-radius:10px 10px 10px 10px;
        }
        </style>""", unsafe_allow_html=True)
        col6.button(label='Extract Features')


if __name__ == '__main__':
    main()
