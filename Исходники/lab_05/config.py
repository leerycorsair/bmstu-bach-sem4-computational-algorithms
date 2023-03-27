import math
from data_classes import ParamLimits, IntegrateLimits

# Parameter limits
PSTART, PEND, PSTEP = 0.05, 10.0, 0.05

# Inner integrate limits
I_LEFT, I_RIGHT = 0, math.pi / 2

# Outer integrate limits
O_LEFT, O_RIGHT = 0, math.pi / 2


PARAM_LIMITS = ParamLimits(PSTART, PEND, PSTEP)

INTEGRATE_LIMITS = [
    IntegrateLimits(I_LEFT, I_RIGHT),
    IntegrateLimits(O_LEFT, O_RIGHT)
]
