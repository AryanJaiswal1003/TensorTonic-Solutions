import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Calculating the Probability of k Success and Probability of n - k failures:
    probability = math.pow(p, k) * math.pow(1 - p, n - k)
    # Caluclating the Probability Mass Function:
    pmf = math.comb(n, k) * probability

    # Calculating the Cumulative Density Function
    cdf = 0
    for i in range(k + 1):
        probability = math.pow(p, i) * math.pow(1 - p, n - i)
        func = math.comb(n, i) * probability
        cdf += func
    
    output = {"pmf": pmf, "cdf": cdf}
    
    return {k: float(v) for k, v in output.items()}