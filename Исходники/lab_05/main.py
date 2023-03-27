from io_funcs import get_nodes, get_parameter, get_integrators
from function import function
from statistics import cmp_integ_value_by_param, graph_label, graph_show
from config import PARAM_LIMITS, INTEGRATE_LIMITS
from integrators import integrate, SimpsonException


def main():

    while True:
        nodes = get_nodes()
        parameter = get_parameter()
        integrators = get_integrators()

        try:
            parameter_integral = lambda parameter: integrate(
                function(parameter), INTEGRATE_LIMITS, nodes, integrators)

            print("Integral value:", parameter_integral(parameter))

            cmp_integ_value_by_param(parameter_integral, PARAM_LIMITS,
                                     graph_label(nodes, integrators))

            continue_condition = int(
                input("Enter 0 to exit or 1 to continue:"))
            if continue_condition == 0:
                break

        except SimpsonException:
            print("Simpson method cannot be applied.")

    graph_show()


if __name__ == "__main__":
    main()