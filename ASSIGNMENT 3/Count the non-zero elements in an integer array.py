def count_non_zero(array):
    return sum(1 for num in array if num != 0)
array = [0, 1, 2, 0, 3, 4]
print("Count of non-zero elements:", count_non_zero(array))