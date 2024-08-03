def compute_series_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += ((-1) ** (i + 1)) / i
    return total
n = int(input("Enter a positive integer n: "))
print("The sum of the series is:", compute_series_sum(n))