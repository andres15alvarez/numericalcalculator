## module bisection
"""
    root = bisection(f,x1,x2,switch=0,tol=1.0e-9).
    Finds a root of f(x) = 0 by bisection.
    The root must be bracketed in (x1,x2).
    Setting switch = 1 returns root = None if
    f(x) increases upon bisection.
"""
import numpy as np


def bisection(f, xl, xu, tol = 1.0e-5, max_iter = 150):
    f1 = f(xl)
    if f1 == 0.0:
        return xl
    f2 = f(xu)
    if f2 == 0.0:
        return xu
    if np.sign(f1) == np.sign(f2):
        raise Exception(f"La ecuacion no tiene raiz en el intervalo [{xl}, {xu}]")
    xr = 0.0

    for _ in range(max_iter):
        xr = xl + ((xu - xl) / 2)
        f3 = f(xr)

        if f3 == 0.0:
            return xr

        if np.abs(f3) < tol:
            return xr

        if np.sign(f1) != np.sign(f3):
            xl = xr
            f1 = f3

        if np.sign(f2) != np.sign(f3):
            xu = xr
            f2 = f3

    return xr
