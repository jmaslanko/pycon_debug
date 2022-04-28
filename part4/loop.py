filename = "my_numbers.txt"


def write_numbers(max_value):
    with open(filename, "w") as f:
        ii = 0
        while ii < max_value:
            if ii % 2 == 0:
                f.write(f"even number: {ii}\n")
            else:
                f.write(f"odd number: {ii}\n")
                ii += 1


write_numbers(max_value=3)
