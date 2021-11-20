import streamlit as st
import cv2
import numpy as np
from PIL import Image
from scipy.ndimage.filters import convolve

vertical_robert_filter = np.array([[1, 0], [0, -1]])
horizontal_robert_filter = np.array([[0, 1], [-1, 0]])

vertical_sobel_filter = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
horizontal_sobel_filter = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

vertical_prewitt_filter = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
horizontal_prewitt_filter = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])


def modification_bar():

    blur = st.radio('Apply Blur', ('No blur', 'Gaussian blur', 'Median blur'))
    thresholding = st.radio('Apply Thresholding', ('No thresholding', 'Mean thresholding', 'Adaptive thresholding'))
    filters = st.radio('Apply Filter', ('No filter', 'Robert filter', 'Sobel filter', 'Prewitt filter'))

    return blur, thresholding, filters


def apply_blur(blur, img):

    if blur == 'Gaussian blur':
        return cv2.GaussianBlur(img, (1, 1), 0)
    elif blur == 'Median blur':
        return cv2.medianBlur(img, 1)
    else:
        return img


def apply_thresholding(thresholding, img):

    if thresholding == 'Mean thresholding':
        th = img.mean()
        return np.array(img > th).astype(int) * 255
    elif thresholding == 'Adaptive thresholding':
        return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    else:
        return img


def apply_filter(filters, img):

    img = Image.fromarray(img)

    if filters == 'Mean thresholding':
        img = convolve(img, vertical_robert_filter)
        img = convolve(img, horizontal_robert_filter)
    elif filters == 'Adaptive thresholding':
        img = convolve(img, vertical_sobel_filter)
        img = convolve(img, horizontal_sobel_filter)
    elif filters == '':
        img = convolve(img, vertical_prewitt_filter)
        img = convolve(img, horizontal_prewitt_filter)

    return img
    

def show_modified_image(blur, thresholding, filters, img):
    
    if st.button("Modify picture"):
        img = apply_blur(blur, img)
        img = apply_thresholding(thresholding, img)
        img = apply_filter(filters, img)

    return img


