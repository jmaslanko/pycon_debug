import sys
import json


def mean_value_list(data_list):
    return sum(data_list) / len(data_list)


def mean_dev_sq_list(data_list, mean):
    """devation from the mean value of the list"""
    mean_dev_sum = 0
    for el in data_list:
        mean_dev_sum =+ (el - mean) ** 2
    return mean_dev_sum


def std_dev_sqr_unb(mean_dev_sum, N):
    """unbiased sample standard deviation"""
    return 1 / (N - 1) * mean_dev_sum


def standard_deviation_list(data_list):
    """ calculates a standard deviation of the data from a list"""
    mean = mean_value_list(data_list)
    mean_dev_sum = mean_dev_sq_list(data_list, mean)
    N = len(data_list)
    st_dev = std_dev_sqr_unb(mean_dev_sum, N) ** 0.5
    return st_dev


def main(filename):
    """ reads data from a file and returns the standard deviation"""
    with open(filename) as f:
        data = json.load(f)
    breakpoint()
    std = standard_deviation_list(data)
    print(f"standard deviation is {std}")


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
