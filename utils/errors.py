import numpy as np


def relative_error(xi: float, xr: float) -> float:
    return np.abs((xr - xi) / xi) * 100
