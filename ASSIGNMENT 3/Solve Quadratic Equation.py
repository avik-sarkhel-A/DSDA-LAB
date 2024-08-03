import cmath
def solve_quadratic_eqn(a, b, c):
    d = (b**2) - (4*a*c)  # Discriminant
    sol1 = (-b + cmath.sqrt(d)) / (2 * a)
    sol2 = (-b - cmath.sqrt(d)) / (2 * a)
    return sol1, sol2
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
solutions = solve_quadratic_eqn(a, b, c)
print("The solutions are:", solutions)