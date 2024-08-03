def sum_and_average(arr):
    total = sum(arr)
    average = total / len(arr) if arr else 0
    return total, average
print(sum_and_average([1, 2, 3, 4, 5]))