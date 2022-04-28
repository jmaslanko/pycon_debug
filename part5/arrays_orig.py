import sys
import json
import numpy as np


def main(filename):
    """ reads data from a file and returns the standard deviation"""
    with open(filename) as f:
        data = json.load(f)
    std = np.std(data)
    print(f"standard deviation from NumPy is {std}")


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
