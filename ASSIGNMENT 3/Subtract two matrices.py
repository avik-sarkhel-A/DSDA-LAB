def subtract_matrices(matrix1, matrix2):
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
matrix1 = [[5, 6], [7, 8]]
matrix2 = [[1, 2], [3, 4]]
result = subtract_matrices(matrix1, matrix2)
print("Result of subtraction:")
for row in result:
    print(row)