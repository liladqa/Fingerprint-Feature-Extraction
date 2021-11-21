from matplotlib import pyplot as plt
from skimage.feature import hessian_matrix, hessian_matrix_eigvals
import cv2


def detect_ridges(gray, sigma= 0.1):
    H_elems = hessian_matrix(gray, sigma=sigma, order='rc')
    maxima_ridges, minima_ridges = hessian_matrix_eigvals(H_elems)
    return maxima_ridges, minima_ridges