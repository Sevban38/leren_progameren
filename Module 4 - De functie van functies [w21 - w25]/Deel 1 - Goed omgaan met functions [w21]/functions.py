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
    return [num for num in range(2, n+1) if is_prime(num)]

def get_n_primes(n):
    primes, num = [], 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def get_primes_between(start, end):
    return [num for num in range(start, end+1) if is_prime(num)]

get_primes_between(1, 10) # Expected: [2, 3, 5, 7]
get_n_primes(5) # Expected: [2, 3, 5, 7, 11]
get_all_primes(10) # Expected: [2, 3, 5, 7]

get_primes_between(50, 90) # Expected: [53, 59, 61, 67, 71, 73, 79, 83, 89]
get_n_primes(10) # Expected: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
get_all_primes(100) # Expected: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]