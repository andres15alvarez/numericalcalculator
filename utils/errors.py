import numpy as np


def relative_error(xi: float, xr: float) -> float:
    if xr == 0:
        return 0
    return np.abs((xr - xi) / xi) * 100
