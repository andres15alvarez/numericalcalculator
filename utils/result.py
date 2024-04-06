from typing import Tuple


class Result:
    def __init__(self, iteration: int, point: Tuple[float, float], error: float) -> None:
        self.iteration = iteration
        self.point = point
        self.error = error
