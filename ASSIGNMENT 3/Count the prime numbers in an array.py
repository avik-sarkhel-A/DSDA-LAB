def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def count_primes(array):
    return sum(1 for num in array if is_prime(num))
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Count of prime numbers:", count_primes(array))