import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = b**2 - 4*a*c
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Roots are:", root1, "and", root2)
elif d == 0:
    root = -b / (2 * a)
    print("Root is:", root)
else:
    realPart = -b / (2 * a)
    imaginaryPart = math.sqrt(-d) / (2 * a)
    print("Roots are:", realPart, "+", imaginaryPart, "i and", realPart, "-", imaginaryPart, "i")
