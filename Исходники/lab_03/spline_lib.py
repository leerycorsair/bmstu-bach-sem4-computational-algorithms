class Cube_Spline():
    def __init__(self, x_l, x_r, a, b, c, d):
        self.x_l = x_l
        self.x_r = x_r
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def value(self, x):
        return self.a + self.b * (x - self.x_l) + self.c * (
            x - self.x_l)**2 + self.d * (x - self.x_l)**3

    def is_x_correct(self, x):
        return self.x_l <= x < self.x_r


def calc_splines(data: list) -> list[Cube_Spline]:
    N = len(data) - 1

    def _h(i: int) -> float:
        return data[i][0] - data[i - 1][0]

    def _ydelta(i: int) -> float:
        return data[i][1] - data[i - 1][1]

    def _f(i: int) -> float:
        return 3 * (_ydelta(i) / _h(i) - _ydelta(i - 1) / _h(i - 1))

    def _xi(i: int) -> float:
        return -_h(i - 1) / (_h(i - 2) * XI_LIST[i - 1] + 2 *
                             (_h(i - 1) + _h(i - 2)))

    def _eta(i: int) -> float:
        return (_f(i - 1) - _h(i - 2) * ETA_LIST[i - 1]) / (
            _h(i - 2) * XI_LIST[i - 1] + 2 * (_h(i - 1) + _h(i - 2)))

    def _a():
        for i in range(N):
            splines.append(
                Cube_Spline(data[i][0], data[i + 1][0], data[i][1], 0, 0, 0))

    def _xi_and_eta():
        for i in range(2, N + 1):
            XI_LIST.append(_xi(i + 1))
            ETA_LIST.append(_eta(i + 1))

    def _c():
        splines[N].c = ETA_LIST[N + 1]
        for i in range(1, N):
            splines[N -
                    i].c = XI_LIST[N - i + 1] * splines[N - i +
                                                        1].c + ETA_LIST[N - i +
                                                                        1]

    def _b():
        splines[N].b = _ydelta(N) / _h(N) - _h(N) * 2 * splines[N].c / 3
        for i in range(1, N):
            splines[i].b = _ydelta(i) / _h(i) - _h(i) * (splines[i + 1].c -
                                                         2 * splines[i].c) / 3

    def _d():
        splines[N].d = -splines[N].c / (3 * _h(N))
        for i in range(1, N):
            splines[i].d = (splines[i + 1].c - splines[i].c) / (3 * _h(N))

    splines: list[Cube_Spline] = [" "]
    XI_LIST: list[float] = [0.0, 0.0, 0.0]
    ETA_LIST: list[float] = [0.0, 0.0, 0.0]
    _a()
    _xi_and_eta()
    _c()
    _b()
    _d()
    return splines
