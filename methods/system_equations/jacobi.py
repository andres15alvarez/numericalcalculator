import numpy as np


def jacobi(A, b, tol = 1e-5, max_iterations = 150):
    x = np.zeros_like(b, dtype=np.double)
    T = A - np.diag(np.diagonal(A))
    counter = 0

    for _ in range(max_iterations):
        x_old  = x.copy()
        counter += 1
        x[:] = (b - np.dot(T, x)) / np.diagonal(A)

        if (np.abs(x - x_old) / np.abs(x) < tol).all():
            return x, counter

    return x, counter
