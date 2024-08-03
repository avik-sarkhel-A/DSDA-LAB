number = int(input("Enter a number: "))
sum_of_divisors = 0
for i in range(1, number):
    if number % i == 0:
        sum_of_divisors += i
if sum_of_divisors == number:
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
num = number
num_str = str(num)
num_digits = len(num_str)
sum_of_powers = 0
while num > 0:
    digit = num % 10
    sum_of_powers += digit ** num_digits
    num //= 10
if sum_of_powers == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
