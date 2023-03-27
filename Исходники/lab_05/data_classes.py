from dataclasses import dataclass


@dataclass
class ParamLimits:
    start: float
    end: float
    step: float

    def __init__(self, start: float, end: float, step: float):
        self.start = start
        self.end = end
        self.step = step


@dataclass
class IntegrateLimits:
    left: float
    right: float

    def __init__(self, left: float, right: float):
        self.left = left
        self.right = right
