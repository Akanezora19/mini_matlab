import math


def det_2by2(matrix):
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    determinant = a * d - b * c
    return determinant


print(det_2by2([[1, 1], [2, 2]]))


def cofactor_det(matrix):
    A = matrix
    n = len(A)
    for i in range(n):
        if len(A[i]) != n:
            return "Please enter a square matrix"
    if n == 1:
        return A[0][0]
    elif n == 2:
        return det_2by2(A)
    else:
        determinant = 0
        for j in range(n):
            submatrix = [[A[row][col] for col in range(n) if col != j] for row in range(1, n)]
            # print(submatrix)
            if len(submatrix) == 2:
                cofactor = (-1) ** j * det_2by2(submatrix)
                determinant += A[0][j] * cofactor
            else:
                cofactor = (-1) ** j * cofactor_det(submatrix)
                determinant += A[0][j] * cofactor
        return determinant


print(cofactor_det([[1, 2, 3], [1, 123, 5], [0, 0, 9]]))


def inv_2by2(matrix):
    det = det_2by2(matrix)
    if det == 0:
        return "Matrix is not invertible"

    inv_det = f"1/{det}"
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    matrix[1][1], matrix[0][0], matrix[0][1], matrix[1][0] = a, d, -b, -c
    return matrix if det == 1 else f"{inv_det}{matrix}"


print(inv_2by2([[1, 1], [2, 9]]))


def matrix_validate(matrix):
    """Check if all rows have the same length"""
    if not matrix:
        return False
    first_row_len = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != first_row_len:
            return False
    return True


def matrix_transpose(matrix):
    """Make every column to be the new row(this is the only way)"""
    if not matrix_validate(matrix):
        print("Please enter a valid matrix")
    else:
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]


print(matrix_transpose([[1, 2, 4], [4, 5, 6], [7, 8, 123], [1, 2, 3]]))


def vector_validate(vector):
    if not vector:
        return False
    elif not isinstance(vector, list):
        return False
    else:
        return True

def dot_product(vector1, vector2):
    if not vector_validate(vector1) or not vector_validate(vector2):
        print("Please enter valid vectors")
    elif len(vector1) != len(vector2):
        print("Please enter vectors with the same length")
    else:
        return sum(a * b for a, b in zip(vector1, vector2))


print(dot_product([2, 3], [3, 4]))


def vector_magnitude(vector):
    if not vector_validate(vector):
        print("Please enter a valid vector")
    else:
        return math.sqrt(sum(a ** 2 for a in vector))


print(vector_magnitude([1, 1]))


def normal_vector(vector):
    if not vector_validate(vector):
        print("Please enter a valid vector")
    else:
        return [(1/vector_magnitude(vector)) * i for i in vector]


print(normal_vector([1, 1]))

def matrix_multiplication(matrix1, matrix2):
    if not matrix_validate(matrix1) or not matrix_validate(matrix2):
        print("Please enter valid matrices")
    elif len(matrix1[0]) != len(matrix2):
        print("Please enter matrices with compatible dimensions")
    else:
        matrix2 = matrix_transpose(matrix2)
        return [[dot_product(matrix1[i],matrix2[j]) for j in range(len(matrix2))] for i in range(len(matrix1))]
print

matrix1 = [[1, 1, 89], [1, 345, 1]]
matrix2 = [[2, 7], [4, 10], [2, 6]]
print(matrix_multiplication(matrix1, matrix2))


def orthogonal_projection(plane, vector):
    """Takes in a vector and project it onto the plane,
    with basis vectors of plane written in matrix A"""
