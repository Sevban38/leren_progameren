from functions import is_prime
from test_lib import test, report
def get_all_primes(n):
    primes = []
    for num in range(2, n+1):
        if is_prime(num):
            primes.append(num)
    return primes

def get_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def get_primes_between(start, end):
    primes = []
    for num in range(start, end+1):
        if is_prime(num):
            primes.append(num)
    return primes

# Tests for get_all_primes
print(get_all_primes(10))  # Output: [2, 3, 5, 7]
print(get_all_primes(20))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]

# Tests for get_n_primes
print(get_n_primes(5))  # Output: [2, 3, 5, 7, 11]
print(get_n_primes(10))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Tests for get_primes_between
print(get_primes_between(10, 20))  # Output: [11, 13, 17, 19]
print(get_primes_between(50, 70))  # Output: [53, 59, 61, 67]