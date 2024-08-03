def is_armstrong_number(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return sum(d ** power for d in digits) == num
print(is_armstrong_number(153))