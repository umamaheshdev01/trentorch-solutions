
import numpy as np


def determinant(a: np.ndarray) -> float:
        return float(np.linalg.det(a))


def is_invertible(a: np.ndarray) -> bool:
    return not np.isclose(determinant(a), 0.0)


def matrix_inverse(a: np.ndarray) -> np.ndarray:
    if not is_invertible(a):
        raise np.linalg.LinAlgError("Matrix is singular and cannot be inverted.")

    return np.linalg.inv(a)
