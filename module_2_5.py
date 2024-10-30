def get_matrix(n, m, value):
    matrix = []
    for i in range(0, n):
        matrix_in_matrix = []
        matrix.append(matrix_in_matrix)
        for j in range(0, m):
            matrix_in_matrix.append(value)
            j += 1
        i += 1
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)