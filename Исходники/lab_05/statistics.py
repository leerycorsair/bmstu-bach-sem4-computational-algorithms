import matplotlib.pyplot as plt
from integrators import simpson
from data_classes import ParamLimits
from numpy import arange


def cmp_integ_value_by_param(parameter_integral, param_limits: ParamLimits,
                             graph_label: str):
    params = arange(param_limits.start, param_limits.end + param_limits.step,
                    param_limits.step)
    integ_values = list()
    for param in params:
        integ_values.append(parameter_integral(param))
    plt.plot(params, integ_values, label=graph_label)


def graph_label(nodes, funcs):
    label = "Nodes ({0},{1});".format(*nodes)
    label += "Simpson" if funcs[0] == simpson else "Gauss"
    label += "-" + ("Simpson" if funcs[1] == simpson else "Gauss")
    return label


def graph_show():
    plt.legend()
    plt.ylabel("Integral value")
    plt.xlabel("Parameter value")
    plt.show()