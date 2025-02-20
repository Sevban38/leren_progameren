# Tests for get_all_primes
test('get_all_primes test 1', [2, 3, 5, 7], get_all_primes(10))
test('get_all_primes test 2', [2, 3, 5, 7, 11, 13, 17, 19], get_all_primes(20))

# Tests for get_n_primes
test('get_n_primes test 1', [2, 3, 5, 7, 11], get_n_primes(5))
test('get_n_primes test 2', [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], get_n_primes(10))

# Tests for get_primes_between
test('get_primes_between test 1', [11, 13, 17, 19], get_primes_between(10, 20))
test('get_primes_between test 2', [53, 59, 61, 67], get_primes_between(50, 70))

# Generate test report
report()