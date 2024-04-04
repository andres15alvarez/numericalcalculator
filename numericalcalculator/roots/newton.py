## module newton
""" root = newton(f,df,a,b,tol=1.0e-5,max).
    Finds a root of f(x) = 0 by combining the Newton-Raphson
    method with bisection. The root must be bracketed in (a,b).
    Calls user-supplied functions f(x) and its derivative df(x).
"""
import numpy as np


def newton(f, df, x, tol = 1.0e-5, max_iter = 150):
    xn = x
    for _ in range(0, max_iter):
        fxn = f(xn)
        if np.abs(fxn) < tol:
            return xn

        dfxn = df(xn)
        if dfxn == 0:
            raise Exception("La derivada da igual a 0")

        xn = xn - fxn/dfxn
    return xn
