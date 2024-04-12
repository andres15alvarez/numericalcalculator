import os
from typing import List
import numpy as np
import matplotlib.pyplot as plt

from settings import BASE_DIR
from utils.result import Result


def generate_image(results: List[Result], filename: str):
    path = os.path.join(BASE_DIR, "static", "images", filename)
    if os.path.exists(path):
        return path
    x = np.array([r.point[0] for r in results])
    y = np.array([r.point[1] for r in results])
    plt.plot(x, y)
    plt.savefig(path)
    plt.clf()
    return path
