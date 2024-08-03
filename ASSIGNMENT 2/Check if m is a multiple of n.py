def is_multiple(m, n):
    return m % n == 0
m = int(input("Enter m: "))
n = int(input("Enter n: "))
print(f"{m} is a multiple of {n}: {is_multiple(m, n)}")