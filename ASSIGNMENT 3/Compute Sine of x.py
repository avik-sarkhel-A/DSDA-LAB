import math
def compute_sin(x, n):
    sin_x = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
        sin_x += term
    return sin_x
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms n: "))
print("The sine of x is:", compute_sin(x, n))