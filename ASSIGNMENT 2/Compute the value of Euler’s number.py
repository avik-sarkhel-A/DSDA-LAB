def compute_euler(n):
    e = 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        e += 1 / factorial
    return e
print(compute_euler(10))