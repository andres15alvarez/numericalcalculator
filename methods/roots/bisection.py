## module bisection
"""
    root = bisection(f,x1,x2,switch=0,tol=1.0e-9).
    Finds a root of f(x) = 0 by bisection.
    The root must be bracketed in (x1,x2).
    Setting switch = 1 returns root = None if
    f(x) increases upon bisection.
"""
import numpy as np

from utils.errors import relative_error
from utils.result import Result


def bisection(f, xl, xu, results: list, tol = 1.0e-5, max_iter = 150):
    f1 = f(xl)
    if f1 == 0.0:
        return xl
    f2 = f(xu)
    if f2 == 0.0:
        return xu
    if np.sign(f1) == np.sign(f2):
        raise Exception(f"La ecuacion no tiene raiz en el intervalo [{xl}, {xu}]")
    xr = 0.0

    for i in range(1, max_iter + 1):
        xr = xl + ((xu - xl) / 2)
        f3 = f(xr)

        if len(results) > 0:
            xr_prev = results[i - 2].point[0]
        else: xr_prev = 0
        error = relative_error(xr, xr_prev)
        results.append(Result(i, (xr, f3), error))

        if error <= tol:
            return xr

        if f3 == 0.0:
            return xr

        if np.sign(f1) != np.sign(f3):
            xu = xr
            f2 = f3

        if np.sign(f2) != np.sign(f3):
            xl = xr
            f1 = f3

    return xr
