
import numpy as np

def rank(A):
    """
    Returns the rank of matrix A.
    """
    return np.linalg.matrix_rank(A)


def nullity(A):
    """
    Returns the nullity of matrix A.
    """
    return A.shape[1] - rank(A)
