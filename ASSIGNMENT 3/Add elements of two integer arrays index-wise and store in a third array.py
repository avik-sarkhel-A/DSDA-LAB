def add_arrays(array1, array2):
    return [a + b for a, b in zip(array1, array2)]
array1 = [1, 2, 3]
array2 = [4, 5, 6]
result = add_arrays(array1, array2)
print("Resultant array:", result)