
import numpy as np

def qr_decompose(A):
    """
    A: an (m, n) NumPy array with linearly independent columns.

    Returns:
        Q: (m, n) matrix with orthonormal columns.
        R: (n, n) upper-triangular matrix.
    """

    A = np.array(A, dtype=float)
    m, n = A.shape

    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):

        # Take the j-th column of A
        v = A[:, j].copy()

        # Remove projections onto previous Q columns
        for i in range(j):

            R[i, j] = np.dot(Q[:, i], A[:, j])

            v = v - R[i, j] * Q[:, i]

        # Calculate the remaining vector's magnitude
        R[j, j] = np.linalg.norm(v)

        # Normalize the vector
        Q[:, j] = v / R[j, j]

    return Q, R
