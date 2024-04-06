from utils.errors import relative_error
from utils.result import Result


def secant(f, a, b, results: list, max_iter = 150):
    """Approximate solution of f(x)=0 on interval [a,b] by the secant method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
        The number of iterations to implement.

    Returns
    -------
    xn : number
        The x intercept of the secant line on the the Nth interval
            m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        The initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0
        for some intercept m_n then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iterations, the secant method fails and return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> secant(f,1,2,5)
    1.6180257510729614
    """
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
        results.append(Result(i, (xn, fxn), relative_error(xn, xn_prev)))

        if f(an)*fxn < 0:
            an = an
            bn = xn
        elif f(bn)*fxn < 0:
            an = xn
            bn = bn
        elif fxn == 0:
            return xn
    return xn
