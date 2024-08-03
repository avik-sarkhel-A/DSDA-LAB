import math
def factorial_series(n):
    series = [math.factorial(i) for i in range(1, n + 1)]
    return series
print(factorial_series(6))