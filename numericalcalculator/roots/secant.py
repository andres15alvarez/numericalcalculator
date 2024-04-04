def secant(f, a, b, max_iter = 150):
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
        print("Secant method fails.")
        return None
    an = a
    bn = b
    xn = None
    for _ in range(max_iter):
        xn = an - f(an)*(bn - an)/(f(bn) - f(an))
        f_xn = f(xn)
        if f(an)*f_xn < 0:
            an = an
            bn = xn
        elif f(bn)*f_xn < 0:
            an = xn
            bn = bn
        elif f_xn == 0:
            return xn
    return xn
