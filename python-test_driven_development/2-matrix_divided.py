#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor div.

    Args:
        matrix: list of lists of integers or floats
        div: number (integer or float) to divide by

    Returns:
        A new matrix with elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats,
                   if rows are not of the same size,
                   or if div is not an int/float.
        ZeroDivisionError: If div is 0.
    """
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg_type)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg_type)
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError(msg_type)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError(msg_size)

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
