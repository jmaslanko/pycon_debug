import sys
from pathlib import Path


def all_files_stat(dirname):
    """ returns dictionary with stat for all the files from dirname"""
    filestat_dicdirnamet = {}
    for el in Path(dirname).iterdir():
        filestat_dict[el] = el.stat()
    return filestat_dict


def sorting(files):
    """ sorting files from smallest to the largest"""
    sorted_files = sorted(files.items(), key=lambda x: x[1])
    return sorted_files


def mean_size(files):
    """ calculating the mean size of the files"""
    sizes = [el.st_size for el in files.values()]
    return sum(sizes) / len(sizes)


def dir_stat(dirname):
    """ providing some directory statistics"""
    breakpoint()
    files_stat = all_files_stat(dirname)
    files_sorted = sorting(files_stat)
    biggest_file = str(files_sorted[-1][0])
    mean = mean_size(files_stat)
    print(f"mean size of the files is {mean}")
    print(f"the biggest file is {biggest_file}")
    # print(f"the biggest file stat {files_stat[biggest_file]}")


if __name__ == "__main__":
    dirname = sys.argv[1]
    dir_stat(dirname)
