from math import cos, sin, exp, pi


def function(param):
    sub_func = lambda theta, phi: 2 * cos(theta) / (1 - (sin(theta)**2) *
                                                    (cos(phi)**2))
    main_func = lambda theta, phi: (4 / pi) * (1 - exp(-param * sub_func(
        theta, phi))) * cos(theta) * sin(theta)
    return main_func


def function_2_to_1(function, theta):
    return lambda phi: function(theta, phi)