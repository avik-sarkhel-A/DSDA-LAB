n = int(input("Enter the upper limit for the Fibonacci series: "))
a = 0
b = 1
print("Fibonacci series up to", n, ":")
while a <= n:
    print(a, end=" ")
    next_number = a + b
    a = b
    b = next_number
