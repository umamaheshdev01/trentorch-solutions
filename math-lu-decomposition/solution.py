
import numpy as np

def lu_decompose(A):
    U = A.copy().astype(float)
    n = U.shape[0]

    L = np.eye(n)

    for k in range(n - 1):
        for i in range(k + 1, n):

            multiplier = U[i, k] / U[k, k]

            L[i, k] = multiplier

            U[i, k:] = U[i, k:] - multiplier * U[k, k:]

    return L, U
