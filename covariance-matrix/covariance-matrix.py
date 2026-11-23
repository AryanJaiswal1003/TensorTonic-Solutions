import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Subtract each feature's mean (axis=0 collapses rows/samples) so 
    # every feature column is centered around 0
    centered = X - np.mean(X, axis = 0)

    # Multiply X_c^Transpose (shape D x N) by X_c (shape N x D) to get the 
    # D x D sum of outer products/cross-deviations
    cov_matrix = np.dot(centered.T, centered)

    # Use N - 1 (Bessel's correction) for unbiased sample covariance; 
    # np.shape(X)[0] is N (number of samples)
    samples = np.shape(X)[0] - 1

    # Divide elementwise by (N - 1) to return the D x D covariance matrix
    return cov_matrix / samples