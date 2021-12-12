import imageio
import skimage
import streamlit as st
from PIL import Image
from matplotlib import pyplot as plt
from skimage.color import rgb2gray
from extraction import getTerminationBifurcation, extractMinutiaeFeatures, ShowResults
from vector import *

from modification import *
import numpy as np
from ridge_detection import detect_ridges


st.set_page_config(layout="wide")

Title_html = open("index.html", 'r', encoding='utf-8')
source_code = Title_html.read()
st.markdown(source_code, unsafe_allow_html=True)

col1, col2, col3 = st.columns([3, 6, 3])
image_file = col2.file_uploader("Upload your fingerprint", type=["tif"])
col4, col5, col6, col7 = st.columns([3, 4.5, 1.5, 3])
col8, col9, col10, col11, col12, col13 = st.columns([3, 1.5, 1.5, 1.5, 1.5, 3])
col14, col15, col16, col17 = st.columns([3, 4.5, 1.5, 3])

placeholder = col5.empty()

def plot_images(*images):
    images = list(images)
    n = len(images)
    fig, ax = plt.subplots(ncols=n, sharey=True, figsize=(12, 12))
    for i, img1 in enumerate(images):
        ax[i].imshow(img1, cmap='gray')
        ax[i].axis('off')
    plt.subplots_adjust(left=0.03, bottom=0.03, right=0.97, top=0.97)
    return fig

def main():

    if image_file is not None:
        original_img = Image.open(image_file)
        placeholder.image(original_img, use_column_width=True, output_format="auto")
        image_data = np.asarray(original_img)
        modified_img = image_data

        with col6.form(key="image_display", clear_on_submit=False):
            blur, tresholding, filters = modification_bar()
            apply = st.form_submit_button("Apply changes")
            if apply:
                modified_img = show_modified_image(blur, tresholding, filters, image_data)
                placeholder.image(modified_img, use_column_width=True, output_format="auto")


        with col10:
            if st.button('Extract features'):
                a, b = detect_ridges(modified_img, sigma=0.9)

                img = np.array(modified_img).astype(int)

                for i, v1 in enumerate(img):
                    for j, v2 in enumerate(v1):
                        if v2 >= 125:
                            img[i, j] = 1
                        else:
                            img[i, j] = 0

                skel = skimage.morphology.skeletonize(img)
                skel = np.uint8(skel) * 255
                mask = img * 255

                (minutiaeTerm, minutiaeBif) = getTerminationBifurcation(skel, mask)
                FeaturesTerm, FeaturesBif = extractMinutiaeFeatures(skel, minutiaeTerm, minutiaeBif)
                BifLabel = skimage.measure.label(minutiaeBif, connectivity=1)
                TermLabel = skimage.measure.label(minutiaeTerm, connectivity=1)
                results = ShowResults(skel, TermLabel, BifLabel)
                extracted = Image.fromarray(results).convert('RGB')
                placeholder.image(extracted, use_column_width=True, output_format="auto")

                col15.success('Fingerprint feature vector = ' + str(determine_vector(FeaturesTerm, FeaturesBif)))


if __name__ == '__main__':
    main()
