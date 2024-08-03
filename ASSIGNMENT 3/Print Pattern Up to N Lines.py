def print_pattern(n):
    for i in range(n):
        if i % 2 == 0:
            print("/\\")
        else:
            print("/  \\")
        if i == n - 1:
            print("/___\\")
n = int(input("Enter the number of lines N: "))
print_pattern(n)