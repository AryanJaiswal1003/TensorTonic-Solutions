import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """    
    ab_norm = np.linalg.norm(a) * np.linalg.norm(b)
    cosine = float(np.dot(a, b) / ab_norm)

    if ab_norm == 0:
        return float(ab_norm)
    return cosine
    