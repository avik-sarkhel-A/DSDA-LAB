def is_sparse(matrix):
    zero_count = sum(row.count(0) for row in matrix)
    return zero_count > (len(matrix) * len(matrix[0])) / 2
matrix = [[0, 0, 3], [4, 0, 0], [0, 0, 0]]
print("Is the matrix sparse?", is_sparse(matrix))