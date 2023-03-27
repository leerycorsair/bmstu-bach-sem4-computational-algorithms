import config
import numpy
import matplotlib.pyplot as plt


class Dot():
    def __init__(self, x, y, p):
        self.x = x
        self.y = y
        self.p = p


class Data():
    def __init__(self):
        self.data: List[Dot] = []

    def load(self):
        f = open(config.DEFAULT_FILE_IN)
        for line in f:
            dot = Dot(*[float(num) for num in line.split(" ")])
            self.data.append(dot)
        f.close()

    def ls_perform(self):
        def calc_coeff(deg):
            coeff = 0
            for dot in self.data:
                coeff += dot.p * dot.x**deg
            return coeff

        def sole_sollution(mtr):
            for i in range(len(mtr)):
                for j in range(len(mtr)):
                    if i == j: continue
                    mult = mtr[j][i] / mtr[i][i]
                    for k in range(len(mtr) + 1):
                        mtr[j][k] -= mult * mtr[i][k]
            for i in range(len(mtr)):
                mult = mtr[i][i]
                for j in range(len(mtr[i])):
                    mtr[i][j] /= mult
            return [mtr[i][-1] for i in range(len(mtr))]

        def add_sole_mtr(mtr):
            for i in range(len(mtr)):
                res = 0
                for dot in self.data:
                    res += dot.p * dot.y * dot.x**i
                mtr[i].append(res)

        def create_sole_mtr(deg):
            mtr = [[calc_coeff(j + i) for i in range(deg + 1)]
                   for j in range(deg + 1)]
            add_sole_mtr(mtr)
            return mtr

        def plot_add_polinom(a_coeffs, deg):
            plot_x, plot_y = [], []
            step = (self.data[-1].x - self.data[0].x) / 1000
            for x in numpy.arange(self.data[0].x, self.data[-1].x + step,
                                  step):
                plot_x.append(x)
                y = 0
                for i in range(len(a_coeffs)):
                    y += a_coeffs[i] * x**i
                plot_y.append(y)
            plt.plot(plot_x, plot_y, label="n = {0}".format(deg))

        def plot_add_dots():
            plot_x = [dot.x for dot in self.data]
            plot_y = [dot.y for dot in self.data]
            plt.plot(plot_x, plot_y, "o", label="Точки")

        def plot_draw():
            plt.legend()
            plt.xlabel("X")
            plt.ylabel("Y")
            plt.grid()
            plt.show()

        for deg in config.POL_DEGS:
            sole_mtr = create_sole_mtr(deg)
            a_coeffs = sole_sollution(sole_mtr)
            plot_add_polinom(a_coeffs, deg)
        plot_add_dots()
        plot_draw()
