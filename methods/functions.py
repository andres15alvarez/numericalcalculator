import numpy as np


def f1b(x):
    return x - np.tan(x)

def get_f1b_range():
    return 1, 2

def f1c(x):
    return np.power(x, 8) - 36 * np.power(x, 7) + 546 * np.power(x, 6) - 453 * np.power(x, 5) \
        + 22449 * np.power(x, 4) - 67284 * np.power(x, 3) + 118124 * np.power(x, 2) - 109584 * x + 40320

def f1cc(x):
    return np.power(x, 8) - 36.001 * np.power(x, 7) + 546 * np.power(x, 6) - 453 * np.power(x, 5) \
        + 22449 * np.power(x, 4) - 67284 * np.power(x, 3) + 118124 * np.power(x, 2) - 109584 * x + 40320

def get_f1c_range():
    return 5.5, 6.5

def f2b(x):
    return np.exp(x) - 3 * np.square(x)

def df2b(x):
    return np.exp(x) - 6 * x

def get_f2b_range():
    return 3, 5

def f2c(x):
    return np.log(x - 1) + np.cos(x - 1)

def df2c(x):
    return (1 / (x - 1)) - np.sin(x - 1)

def get_f2c_range():
    return 1.3, 2

A = np.array([
    [5, 8, 3],
    [6, 2, 4],
    [9, 3, 1]
])

B = np.array([
    [8, 5, 6],
    [3, 6, 9],
    [2, 4, 7]
])

C = np.array([
    [8, 5, 6],
    [12, 9, 3],
    [1, 4, 15]
])


matrix1 = np.array([
    [8, 2, -2],
    [10, 2, 4],
    [12, 2, 2]
])
b1 = np.array([-2, 4, 6])


matrix2 = np.array([
    [3, 0.1, -0.2],
    [0.1, 7, -0.3],
    [0.3, -0.2, 10]
])
b2 = np.array([7.85, -19.3, 71.4])
