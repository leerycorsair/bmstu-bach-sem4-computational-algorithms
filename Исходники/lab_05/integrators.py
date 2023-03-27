from data_classes import IntegrateLimits
from function import function_2_to_1

from numpy.polynomial.legendre import leggauss


class SimpsonException(Exception):
    pass


def integrate(func, int_limits: list[IntegrateLimits], nodes: tuple[int],
              int_funcs: list):
    inner_int_func = lambda theta: int_funcs[1](function_2_to_1(func, theta),
                                                int_limits[1], nodes[1])

    return int_funcs[0](inner_int_func, int_limits[0], nodes[0])


def simpson(func, int_limits: IntegrateLimits, nodes_amount: int):

    if (nodes_amount < 3 or nodes_amount % 2 == 0):
        raise SimpsonException

    h = (int_limits.right - int_limits.left) / (nodes_amount - 1)
    x = int_limits.left
    int_value = 0

    for iteration in range((nodes_amount - 1) // 2):
        int_value += func(x) + 4 * func(x + h) + func(x + 2 * h)
        x += 2 * h

    return int_value * h / 3


def gauss(func, int_limits: IntegrateLimits, nodes_amount: int):
    t_list, a_list = leggauss(nodes_amount)

    int_value = 0

    for i in range(nodes_amount):
        int_value += (int_limits.right -
                      int_limits.left) / 2 * a_list[i] * func(
                          arg_format(t_list[i], int_limits))

    return int_value


def arg_format(t: float, int_limits: IntegrateLimits):
    return (int_limits.left + int_limits.right) / 2 + (int_limits.right -
                                                       int_limits.left) * t / 2
