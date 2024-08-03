def is_valid(number):
    return number % 7 == 0 and number % 5 != 0
print("Numbers between 1000 and 2000 divisible by 7 but not multiples of 5:")
for number in range(1000, 2001):
    if is_valid(number):
        print(number)
