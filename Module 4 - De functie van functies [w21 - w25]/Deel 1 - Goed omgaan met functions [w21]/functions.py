# Controleert of een getal een priemgetal is.
def is_prime(number:int) -> bool:
    # ...
    if number <= 1:
        return False
    
    # ...
    if number == 2:
        return True
    
    # ...
    if number % 2 == 0:
        return False
    
    # ...
    max_divisor = int(number**0.5) + 1
    for d in range(3, max_divisor, 2):
        if number % d == 0:
            return False
    
    # ...
    return True

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