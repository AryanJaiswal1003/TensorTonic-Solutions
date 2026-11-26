import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Convert Input List to a Numpy Array (shape: N samples x D features)
    data = np.asarray(X, dtype = float)
    num_samples = data.shape[0]

    # 1. Center the data by substracting mean of each feature (column)
    feature_mean = np.mean(data, axis = 0)
    centered = data - feature_mean

    # 2. Sample Covariance Matrix:
    cov_mat = np.dot(centered.T, centered) / (num_samples - 1)

    # 3. Extract feature Standard Deviations from the diagonal of the Covariance Matrix
    feature_stds = np.sqrt(np.diag(cov_mat))

    # 4. Denominator Matrix of Pairwise Standard Deviation (sigma_i * sigma_j)
    std_outer_product = np.outer(feature_stds, feature_stds)

    # Normalized covariance by the product of Standard Deviation
    corr_matrix = cov_mat / std_outer_product

    return corr_matrix