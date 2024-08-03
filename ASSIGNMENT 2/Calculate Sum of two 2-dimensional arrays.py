def sum_of_matrices(mat1, mat2):
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print(sum_of_matrices(mat1, mat2)) 