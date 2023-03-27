FILENAME_IN = "data.txt"


def data_read(filename: str) -> list:
    data: list = []
    f = open(filename, "r")
    for line in f:
        data.append(str_to_num_arr(line))
    f.close()
    return data


def str_to_num_arr(string: str) -> list:
    return [float(value) for value in string.split(" ")]
