In Binomial PMF/CDF calculations, `math.comb` gives the exact number of success combinations while `math.pow` computes the `float` probabilities of successes and failures.



- `math.pow(x, y)`: Computes $x^y$ and **always returns a **`float` (supports non-integer powers).



- `math.comb(n, k)`: Computes $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ and **returns an exact **`int` (returns `0` when $k &lt; 0\  or\  k &gt; n$).