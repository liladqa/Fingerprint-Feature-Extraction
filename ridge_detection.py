from skimage.feature import hessian_matrix, hessian_matrix_eigvals


def detect_ridges(gray, sigma):
    H_elems = hessian_matrix(gray, sigma=sigma, order='rc')
    maxima_ridges, minima_ridges = hessian_matrix_eigvals(H_elems)
    return maxima_ridges, minima_ridges
