def gaussian_eliminate(A, b):

    A = A.astype(float).copy()
    b = b.astype(float).copy()

    n = len(b)

    for i in range(n):
        for j in range(i + 1, n):

            factor = A[j, i] / A[i, i]

            A[j] = A[j] - factor * A[i]
            b[j] = b[j] - factor * b[i]

    return A, b


def back_substitute(U, c):

    n = len(c)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):

        total = 0

        for j in range(i + 1, n):
            total += U[i, j] * x[j]

        x[i] = (c[i] - total) / U[i, i]

    return x
