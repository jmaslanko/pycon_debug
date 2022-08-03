"""
Calculating unbiased standard deviation
https://en.wikipedia.org/wiki/Standard_deviation#Corrected_sample_standard_deviation
"""

import sys
import json
# Test

def mean_value_list(data_list):
    if len(data_list) > 0:
        return sum(data_list) / len(data_list)
    else:
        print(f"List has a size of 0")


def mean_dev_sq_list(data_list, mean):
    """devation from the mean value of the list"""
    mean_dev_sum = 0
    for el in data_list:
        mean_dev_sum =+ (el - mean) ** 2
    return mean_dev_sum


def std_dev_sqr_unb(mean_dev_sum, N):
    """unbiased sample standard deviation"""
    if N > 1:
        return 1 / (N - 1) * mean_dev_sum
    else:
        return 0


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
    std = standard_deviation_list(data)
    print(f"standard deviation is {std}")


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
