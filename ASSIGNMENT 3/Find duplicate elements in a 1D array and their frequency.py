def find_duplicates(array):
    frequency = {}
    for num in array:
        frequency[num] = frequency.get(num, 0) + 1
    return {num: count for num, count in frequency.items() if count > 1}
array = [1, 2, 3, 1, 2, 4]
duplicates = find_duplicates(array)
print("Duplicate elements and their frequency:", duplicates)