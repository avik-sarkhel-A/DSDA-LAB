def calculate_slope(y2, y1, x2, x1):
    if x2 - x1 == 0:
        raise ValueError("Cannot calculate slope for vertical line")
    return (y2 - y1) / (x2 - x1)
y1 = float(input("Enter y1: "))
y2 = float(input("Enter y2: "))
x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))
print("The slope is:", calculate_slope(y2, y1, x2, x1))