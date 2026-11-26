import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    # Convert Input List into 2D square Numpy float array
    square_matrix = np.asarray(matrix, dtype=float)

    # Computing Eigenvalues (Unsorted by Default)
    eigenvalues = np.linalg.eigvals(square_matrix)

    # Sorting and Returning Eigenvalues in Ascending Order
    return np.sort(eigenvalues)
    