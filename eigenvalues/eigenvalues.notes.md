**Eigenvalues &amp; Eigenvectors**



**Core Intuition:** When a square matrix $A$ transforms space, most vectors get knocked off their span (rotated + scaled). 

- `Eigenvectors (`$v$`)` are the special non-zero vectors that stay on their exact same line/direction—they only get stretched or squished.
- `Eigenvalue (`$\lambda$`):` The scalar factor by which the eigenvector is stretched, shrunk, or flipped ($\lambda &lt; 0$ reverses direction; $\lambda = 0$ squashes it to the origin).
- `Fundamental Equation:`** **$A v = \lambda v$



**Characteristic Equation (How to find **$\lambda$**):**

  

$$\det(A - \lambda I) = 0$$

  _(Solving this polynomial gives the eigenvalues; plugging each _$\lambda$_ back into _$(A - \lambda I)v = 0$_ gives the corresponding eigenvectors.)_



**Key ML Takeaway:** 

In **PCA (Principal Component Analysis)**, the eigenvectors of the covariance matrix represent the principal directions (axes of maximum variance), and their corresponding eigenvalues measure how much variance lies along each axis.