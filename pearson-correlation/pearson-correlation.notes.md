## NumPy Functions – Pearson Correlation



- `np.asarray(X, dtype=float)`: Converts input list to a 2D float array `(N, D)` for vectorized math.

- `np.mean(data, axis=0)`: Computes column-wise (feature) means across samples, returning shape `(D,)`.

- `np.dot(centered.T, centered)`: Multiplies `(D, N) @ (N, D)` to get sum of squared deviations/cross-products before dividing by `N - 1`.

- `np.diag(cov_mat)`: Extracts the main diagonal (feature variances $\sigma_i^2$) as a 1D array.

- `np.sqrt(...)`: Converts 1D feature variances into standard deviations ($\sigma_i$).

- `np.outer(feature_stds, feature_stds)`: Builds the `(D, D)` denominator matrix where cell `(i, j)` is $\sigma_i \times \sigma_j$.