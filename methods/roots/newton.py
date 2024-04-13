## module newton
""" root = newton(f,df,a,b,tol=1.0e-5,max).
    Finds a root of f(x) = 0 by combining the Newton-Raphson
    method with bisection. The root must be bracketed in (a,b).
    Calls user-supplied functions f(x) and its derivative df(x).
"""
import numpy as np

from utils.errors import relative_error
from utils.result import Result


def newton(f, df, x, results: list, tol = 1.0e-5, max_iter = 150):
    xn = x
    for i in range(1, max_iter + 1):
        fxn = f(xn)

        if len(results) > 0:
            xn_prev = results[i - 2].point[0]
        else: xn_prev = 0
        error = relative_error(xn, xn_prev)
        results.append(Result(i, (xn, fxn), error))

        if error <= tol:
            return xn

        if np.abs(fxn) < tol:
            return xn

        dfxn = df(xn)
        if dfxn == 0:
            raise Exception("La derivada da igual a 0")

        xn = xn - fxn/dfxn
    return xn
