def generate_combinations():
    combinations = []
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                combinations.append((i, j, k))
    return combinations
print(generate_combinations())