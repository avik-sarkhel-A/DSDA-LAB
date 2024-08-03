def sum_of_odd_numbers(matrix):
    total = 0
    for row in matrix:
        for num in row:
            if num % 2 != 0:
                total += num
    return total
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Sum of odd numbers:", sum_of_odd_numbers(matrix))