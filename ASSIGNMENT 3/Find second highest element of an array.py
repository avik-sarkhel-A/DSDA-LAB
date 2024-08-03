def second_highest(array):
    unique_elements = list(set(array))
    unique_elements.sort()
    return unique_elements[-2] if len(unique_elements) >= 2 else None
array = [1, 2, 3, 4, 5]
print("Second highest element:", second_highest(array))