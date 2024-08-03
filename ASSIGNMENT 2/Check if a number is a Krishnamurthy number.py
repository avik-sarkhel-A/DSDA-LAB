import math
def is_krishnamurthy(n):
    sum_factorials = sum(math.factorial(int(digit)) for digit in str(n))
    return sum_factorials == n
print(is_krishnamurthy(145))