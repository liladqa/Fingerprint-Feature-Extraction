import imageio
import skimage
import streamlit as st
from PIL import Image
from matplotlib import pyplot as plt
from skimage.color import rgb2gray
from extraction import getTerminationBifurcation, extractMinutiaeFeatures, ShowResults

from modification import *
import numpy as np
from ridge_detection import detect_ridges


@st.cache
def load_image():
    img = imageio.imread(image_file)
    return img

st.set_page_config(layout="wide")

Title_html = open("index.html", 'r', encoding='utf-8')
source_code = Title_html.read()
st.markdown(source_code, unsafe_allow_html=True)

col1, col2, col3 = st.columns([3, 6, 3])
image_file = col2.file_uploader("Upload your fingerprint", type=["png", "jpg", "jpeg", "tif", "bmp"])
col4, col5, col6, col7 = st.columns([3, 4.5, 1.5, 3])
col8, col9, col10, col11, col12, col13 = st.columns([3, 1.5, 1.5, 1.5, 1.5, 3])


def main():

    if image_file is not None:
        original_img = Image.open(image_file)
        image_data = np.asarray(original_img)
        modified_img = image_data

        with col5:
            st.markdown('Original Image')
            st.image(original_img, use_column_width=True)

        with col6:
            blur, tresholding, filters = modification_bar()

        with col10:
            st.markdown('Modify Image')

            if st.button('Extract'):

                modified_img = show_modified_image(blur, tresholding, filters, image_data)


                a, b = detect_ridges(modified_img, sigma=0.9)
                # podglad, mozna pozniej wywalic

                def plot_images(*images):
                    images = list(images)
                    n = len(images)
                    fig, ax = plt.subplots(ncols=n, sharey=True, figsize=(12, 12))
                    for i, img1 in enumerate(images):
                        ax[i].imshow(img1, cmap='gray')
                        ax[i].axis('off')
                    plt.subplots_adjust(left=0.03, bottom=0.03, right=0.97, top=0.97)
                    return fig

                st.pyplot(plot_images(a, b))

                # podlad, mozna pozniej wywalic
                st.image(modified_img)

                img = np.array(modified_img).astype(int)

                for i, v1 in enumerate(img):
                    for j, v2 in enumerate(v1):
                        if v2 == 255:
                            img[i, j] = 1

                skel = skimage.morphology.skeletonize(img)
                skel = np.uint8(skel) * 255
                mask = img * 255

                (minutiaeTerm, minutiaeBif) = getTerminationBifurcation(skel, mask)
                FeaturesTerm, FeaturesBif = extractMinutiaeFeatures(skel, minutiaeTerm, minutiaeBif)
                BifLabel = skimage.measure.label(minutiaeBif, connectivity=1)
                TermLabel = skimage.measure.label(minutiaeTerm, connectivity=1)
                results = ShowResults(skel, TermLabel, BifLabel)
                st.image(Image.fromarray(results).convert('RGB'))


if __name__ == '__main__':
    main()