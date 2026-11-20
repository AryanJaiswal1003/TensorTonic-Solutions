from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    mode = Counter(x)
    output = {
        "mean": np.mean(x),
        "median": np.median(x),
        "mode": min(mode) if max(mode.values()) == min(mode.values()) else mode.most_common(1)[0][0]
    }
    return {k: float(v) for k, v in output.items()}