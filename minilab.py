import math

def m_print(matrix):
    matrix_str = ""
    for row in matrix:
        matrix_str += str(row) + "\n"
    return matrix_str

def det_2by2(matrix):
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    determinant = a * d - b * c
    return determinant

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

def inv_2by2(matrix):
    det = det_2by2(matrix)
    if det == 0:
        return "Matrix is not invertible"

    inv_det = f"1/{det}"
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    matrix[1][1], matrix[0][0], matrix[0][1], matrix[1][0] = a, d, -b, -c
    return matrix if det == 1 else f"{inv_det}{m_print(matrix)}"

def matrix_validate(matrix):
    """Check if all rows have the same length"""
    if not matrix:
        return False
    first_row_len = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != first_row_len:
            return False
    return True

def sqaure_matrix_validate(matrix):
    if not matrix_validate(matrix):
        return False
    if len(matrix[0]) != len(matrix[1]):
        return False
    return True
    
def transpose(matrix):
    """Make every column to be the new row(this is the only way)"""
    if not matrix_validate(matrix):
        print("Please enter a valid matrix")
    else:
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

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

def vector_magnitude(vector):
    if not vector_validate(vector):
        print("Please enter a valid vector")
    else:
        return math.sqrt(sum(a ** 2 for a in vector))

def normal_vector(vector):
    if not vector_validate(vector):
        print("Please enter a valid vector")
    else:
        return [(1/vector_magnitude(vector)) * i for i in vector]

def matrix_multiplication(matrix1, matrix2):
    if not matrix_validate(matrix1) or not matrix_validate(matrix2):
        print("Please enter valid matrices")
    elif len(matrix1[0]) != len(matrix2):
        print("Please enter matrices with compatible dimensions")
    else:
        matrix2 = transpose(matrix2)
        return [[dot_product(matrix1[i],matrix2[j]) for j in range(len(matrix2))] for i in range(len(matrix1))]

def rref(matrix):
    pivot = 0
    row_num = len(matrix)
    col_num = len(matrix[0])
    for r in range(row_num):
        if pivot >= col_num:
            return matrix
        i = r
        while matrix[i][pivot] == 0:
            i += 1
            if i == row_num:
                i = r
                pivot += 1
                if col_num == pivot:
                    return matrix
        matrix[i], matrix[r] = matrix[r], matrix[i]
        pivot_value = matrix[r][pivot]
        matrix[r] = [mrx / float(pivot_value) for mrx in matrix[r]]
        for i in range(row_num):
            if i != r:
                pivot_value = matrix[i][pivot]
                matrix[i] = [iv - pivot_value*rv for rv,iv in zip(matrix[r], matrix[i])]
        pivot += 1
    return matrix

def identity_matrix(length):
    matrix = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            if i == j:
                matrix[i][j] = 1
    return matrix
    
def inv(matrix):
    row_num = len(matrix)
    col_num = len(matrix[0])
    eye = identity_matrix(row_num)
    if not sqaure_matrix_validate(matrix):
        return "Please enter a square matrix"
    elif cofactor_det(matrix) == 0:
        return "Please enter an invertible matrix"
    for i in range(row_num):
        matrix[i] += eye[i]
    rref(matrix)
    for i in range(row_num):
        matrix[i] = matrix[i][row_num:]
    return matrix

def transformation(matrix, vector):
    if len(matrix[0]) != len(vector):
        return "Please enter a valid pair"
    final_vector = []
    for row in matrix:
        entry = final_vector.append(dot_product(row, vector))
    return final_vector

def proj(plane, vector):
    """Takes in a vector and project it onto the plane,
    with basis vectors of plane written in matrix A"""
    A = plane
    At = transpose(A)
    result1 = matrix_multiplication(A ,inv(matrix_multiplication(At, A)))
    final_result = transformation(matrix_multiplication(result1, At), vector)
    return final_result
    

#  ----------------------Testing Zone------------------------------

matrix1 = [[1, 1, 89], [1, 345, 1]]
matrix2 = [[2, 7], [4, 10], [2, 6]]
matrix3 = [[1,2,3], [4,5,6], [1,6,9]]

plane1 = [[1,2],[2,9],[0,6],[9,1]]
vector1 = [4,9]
vector2 = [1,2,3,4]

print(cofactor_det([[1, 2, 3], [1, 123, 5], [0, 0, 9]]))
print(m_print(transpose([[1, 2, 4], [4, 5, 6], [7, 8, 123], [1, 2, 3]])))
print(m_print(inv(matrix3)))
print(inv_2by2([[1, 1], [2, 9]]))
print(proj(plane1, vector2))
print(transformation(plane1, vector1))
print(det_2by2([[1, 1], [2, 2]]))
print(m_print(matrix_multiplication(matrix1, matrix2)))
print(m_print(rref(matrix1)))
print(m_print(identity_matrix(9)))
print(vector_magnitude([1, 1]))
print(normal_vector([1, 1]))
print(dot_product([2, 3], [3, 4]))

