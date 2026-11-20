import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Calculating the Variance and the Mean
    centered = x - np.mean(x)
    variance = np.sum(centered ** 2) / (len(x) - 1)

    # Logging the Output
    output = {
        "variance": variance,
        "standard_deviation": np.sqrt(variance)
    }
    # Converting the Values into Float
    return {k: float(v) for k, v in output.items()}