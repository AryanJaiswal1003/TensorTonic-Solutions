import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    rows, cols = np.shape(A)
    transpose = np.zeros((cols, rows))

    for i in range(rows):
        for j in range(cols):
            transpose[j, i] = A[i][j]
    return transpose
            