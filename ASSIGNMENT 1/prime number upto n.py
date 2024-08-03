n = int(input("Enter the upper limit: "))
print(f"Prime numbers up to {n}:")
for num in range(2, n + 1): 
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
