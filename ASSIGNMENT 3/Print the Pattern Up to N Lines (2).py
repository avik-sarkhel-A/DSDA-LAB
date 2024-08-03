def print_complex_pattern(n):
    num = 1
    for i in range(1, n + 1):
        if i % 2 == 1:  # Odd row
            for j in range(1, i + 1):
                print(num, end=" ")
                num += 1
        else:  # Even row
            start = num + i - 1
            for j in range(start, start - i, -1):
                print(j, end=" ")
            num += i
        print()
n = int(input("Enter the number of lines N: "))
print_complex_pattern(n)