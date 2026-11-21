import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    pmf = [(1 - p) if num == 0 else p for num in x]
    output = {
        "pmf": np.array(pmf),
        "mean": float(p),
        "variance": float(p * (1 - p))
    }
    return output