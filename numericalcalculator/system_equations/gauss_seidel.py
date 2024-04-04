import numpy as np


def gauss_seidel(A, b, tol = 1e-5, max_iterations = 150):
    x = np.zeros_like(b, dtype=np.double)
    e = x.copy()

    for _ in range(max_iterations):
        x_old  = x.copy()

        for i in range(A.shape[0]):
            x[i] = (b[i] - np.dot(A[i,:i], x[:i]) - np.dot(A[i,(i+1):], x_old[(i+1):])) / A[i ,i]
            e[i] = np.abs((x[i] - x_old[i]) / x[i])
            if e.all() < tol:
                return x
    return x
