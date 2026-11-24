import numpy as np


def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Normalizes a 2D numeric matrix along a given axis using an L1, L2, or max norm.
    Returns a NumPy array with the same shape as matrix.
    """
    # Convert input list to a float NumPy array once for consistent math and broadcasting
    arr = np.asarray(matrix, dtype=float)

    # Translate norm_type ("max", "l1", "l2", etc.) into NumPy's `ord` argument
    norm = np.inf if norm_type == "max" else int(norm_type[1])

    # Compute the norm over all elements when axis is None
    if axis is None:
        # Flatten -> axis=None computes a vector norm rather than a matrix norm
        output = np.linalg.norm(arr.ravel(), ord=norm)
    else:
        # Keep reduced dimensions so the resulting norm array broadcasts back over `arr`
        output = np.linalg.norm(arr, axis=axis, ord=norm, keepdims=True)

    # Replace zero norms with 1.0 to avoid division by zero
    output = np.where(output == 0, 1, output)

    # Scale each entry by its corresponding norm to return the normalized array
    return arr / output