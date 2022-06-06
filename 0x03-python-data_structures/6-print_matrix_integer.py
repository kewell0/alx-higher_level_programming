#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for a in range(len(row)):
            if a == len(row) - 1:
                print("{:d}".format(row[a]), end="")
            else:
                print("{:d} ".format(row[a]), end="")
        print()
