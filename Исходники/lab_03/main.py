import io_lib
import spline_lib


def main() -> None:
    data = io_lib.data_read(io_lib.FILENAME_IN)
    splines = spline_lib.calc_splines(data)
    x = float(input("X_Value:"))
    for i in range(1, len(splines)):
        if splines[i].is_x_correct(x):
            y = splines[i].value(x)
            print("Y_Value:", y)
            break

if __name__ == "__main__":
    main()