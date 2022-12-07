#!/usr/bin/python3
"""compute the square value of integers of a matrix"""


def square_matrix_simple(matrix=[]):
    new_matrix = [[x ** 2 for x in row] for row in matrix]
    return new_matrix
