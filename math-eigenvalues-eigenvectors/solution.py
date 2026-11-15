
import numpy as np

def eigen_decomposition(a: np.ndarray):
    """
    Returns eigenvalues and eigenvectors of a symmetric matrix.
    Eigenvalues are sorted in ascending order.
    """
    eigenvalues, eigenvectors = np.linalg.eigh(a)

    return eigenvalues, eigenvectors


def verify_eigenpair(a: np.ndarray, eigenvalue: float, eigenvector: np.ndarray) -> bool:
    """
    Checks whether A @ v = eigenvalue * v.
    """
    return np.allclose(
        a @ eigenvector,
        eigenvalue * eigenvector
    )
