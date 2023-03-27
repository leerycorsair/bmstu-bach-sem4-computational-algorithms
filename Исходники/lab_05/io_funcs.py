from integrators import gauss, simpson


def get_nodes() -> tuple[int, int]:
    inner_nodes = int(input("Inner nodes:"))
    outer_nodes = int(input("Outer nodes:"))

    return inner_nodes, outer_nodes


def get_parameter() -> float:
    param = float(input("Parameter value:"))

    return param


def get_integrators():
    SIMPSON = 0
    GAUSS = 1

    inner_mode = int(input("Inner mode: "))
    outer_mode = int(input("Outer mode: "))

    inner_func = gauss if inner_mode == GAUSS else simpson
    outer_func = gauss if inner_mode == GAUSS else simpson

    return outer_func, inner_func