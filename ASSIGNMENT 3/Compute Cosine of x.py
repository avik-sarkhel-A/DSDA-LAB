def compute_cos(x, n):
    cos_x = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
        cos_x += term
    return cos_x
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms n: "))
print("The cosine of x is:", compute_cos(x, n))