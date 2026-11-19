**Transposing a NumPy Array Without **`.T`** or **`.transpose()`

- **Core Concept.** You can flip rows and columns of a 2D array without `.T` or `.transpose()` using axis helpers, Einstein summation, or standard Python logic.
- **Sample Input.** `matrix = np.array([[1, 2, 3], [4, 5, 6]])`
- **Target Output.** `[[1, 4], [2, 5], [3, 6]]`

---
**1.** `np.swapaxes()` **(Best Built-In Alternative)**

- **How it works.** Interchanges two specific axes directly.
- **2D usage.** Swapping axis `0` (rows) and axis `1` (columns) produces an exact transpose.
- **Code.** `transposed = np.swapaxes(matrix, 0, 1)`

---
**2.** `np.moveaxis()`

- **How it works.** Shifts an axis to a new target position.
- **2D usage.** Moving axis `0` to position `1` (or `-1`) flips the matrix.
- **Code.** `transposed = np.moveaxis(matrix, 0, 1)`

---
**3.** `np.einsum()` **(Einstein Summation)**

- **How it works.** Reorders array indices explicitly using string subscripts.
- **2D usage.** Changing `'ij'` to `'ji'` swaps row and column positions.
- **Code.** `transposed = np.einsum('ij->ji', matrix)`

---
**4.** `zip(*matrix)` **(Pure Python / Interview Approach)**

- **How it works.** Unpacks rows into Python's built-in `zip()` to group elements by column, then converts back to an array.
- **Best for.** Coding interviews or tests where NumPy axis functions are restricted.
- **Code.** `transposed = np.array(list(zip(*matrix)))`
