#!/usr/bin/python3
""" A function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ A function that divides all elements of a matrix

        Arguments: the matrix and a div

        Return: A new matrix with values divided by div,
                rounded to 2 decimal places
    """

    mes1 = "matrix must be a matrix (list of lists) of integers/floats"
    mes2 = "Each row of the matrix must have the same size"

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in (int, float):
                raise TypeError(f"{mes1}")
            elif len(matrix[0]) != len(matrix[i]):
                raise TypeError(f"{mes2}")
        if type(matrix) is not list:
            raise TypeError(f"{mes1}")
        elif type(matrix[i]) is not list:
            raise TypeError(f"{mes1}")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(j / div, 2) for j in i] for i in matrix]
