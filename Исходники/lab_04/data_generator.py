import config
import random
import time


def format_float(num):
    return "{:.3f}".format(num)


def num_with_delta(num):
    return num * (1 - config.FUNC_DELTA) + random.random() * (
        num * 2 * config.FUNC_DELTA)


def create_dot(x):
    return (format_float(x) + " " +
            format_float(num_with_delta(config.MY_FUNC(x))) + " " +
            str(random.randint(config.MIN_P, config.MAX_P)) + "\n")


def generate():
    f = open(config.DEFAULT_FILE_OUT, "w")
    x_s = config.X_START
    x_e = config.X_END
    while x_s <= x_e:
        f.write(create_dot(x_s))
        x_s += config.STEP
    f.close()


if __name__ == "__main__":
    random.seed(time.time())
    generate()