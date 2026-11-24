### Quick Notes: NumPy Helpers for Normalization



- `np.linalg.norm(x, ord=..., axis=..., keepdims=...)`

- Computes vector or matrix norms (`ord`: `1`, `2`, `np.inf`, etc.).
- Use `keepdims=True` along an `axis` so the reduced norm stays 2D/broadcastable back onto the original array.
- Note: On a 2D array with `axis=None`, it computes a **matrix norm**, not a flat vector norm.

---

- `np.where(condition, x, y)`

- Vectorized ternary: returns `x` where `condition` is `True`, else `y`.
- Great for safe division: `np.where(norm == 0, 1, norm)` replaces zero norms with `1` so zero slices stay `0` without `ZeroDivisionError` / `NaN` spikes.

---

- `np.ravel(arr)`** (or **`arr.ravel()`**)**

- Collapses an array into a 1D view (when possible without copying).
- Useful before `np.linalg.norm(..., axis=None)` to take a global vector norm across all entries.

---

- **Why **`np.ravel()`** over **`ndarray.flatten()`**?**

- `ravel()`** returns a view when contiguous** $\rightarrow$ faster and uses less memory (no data copy unless required).
- `flatten()`** always returns a new copy** $\rightarrow$ safer if you intend to mutate the 1D array independently, but wasteful for read-only operations like computing a norm.