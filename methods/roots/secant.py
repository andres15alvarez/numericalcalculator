from utils.errors import relative_error
from utils.result import Result


def secant(f, a, b, results: list, tol = 1.0e-5, max_iter = 150):
    if f(a)*f(b) >= 0:
        raise Exception("No hay raiz en el intervalo")
    an = a
    bn = b
    xn = None
    for i in range(1, max_iter + 1):
        xn = an - f(an)*(bn - an)/(f(bn) - f(an))
        fxn = f(xn)

        if len(results) > 0:
            xn_prev = results[i - 2].point[0]
        else: xn_prev = 0
        error = relative_error(xn, xn_prev)
        results.append(Result(i, (xn, fxn), error))

        if error <= tol:
            return xn

        if f(an)*fxn < 0:
            an = an
            bn = xn
        elif f(bn)*fxn < 0:
            an = xn
            bn = bn
        elif fxn == 0:
            return xn
    return xn
