from config import DATA_FILE
from data import data_read, data_print
from differ_methods import differ_methods


def main():
    data = data_read(DATA_FILE)
    data_print(data)
    differ_methods(data)


if __name__ == "__main__":
    main()