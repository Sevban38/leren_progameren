def test_is_prime():
    # Test case 1: number is 0
    assert is_prime(0) == False

    # Test case 2: number is 1
    assert is_prime(1) == False

    # Test case 3: number is 2
    assert is_prime(2) == True

    # Test case 4: number is 3
    assert is_prime(3) == True

    # Test case 5: number is 4
    assert is_prime(4) == False

    # Test case 6: number is 17
    assert is_prime(17) == True

def test_get_all_primes():
    # Test case 1: n is 0
    assert get_all_primes(0) == []

    # Test case 2: n is 10
    assert get_all_primes(10) == [2, 3, 5, 7]

    # Test case 3: n is 20
    assert get_all_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

def test_get_primes_between():
    # Test case 1: start is 0, end is 10
    assert get_primes_between(0, 10) == [2, 3, 5, 7]

    # Test case 2: start is 10, end is 20
    assert get_primes_between(10, 20) == [11, 13, 17, 19]

    # Test case 3: start is 20, end is 30
    assert get_primes_between(20, 30) == [23, 29]

test_is_prime()
test_get_all_primes()
test_get_primes_between()from functions import get_n_primes

def test_get_n_primes():
    # Test case 1: n = 0
    assert get_n_primes(0) == []

    # Test case 2: n = 1
    assert get_n_primes(1) == [2]

    # Test case 3: n = 5
    assert get_n_primes(5) == [2, 3, 5, 7, 11]

    # Test case 4: n = 10
    assert get_n_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]from functions import getPersonCashInGold

def test_getPersonCashInGold():
    # Test case 1: person has no cash
    personCash = {}
    assert getPersonCashInGold(personCash) == 0

    # Test case 2: person has only copper
    personCash = {'copper': 100}
    assert getPersonCashInGold(personCash) == 0.01

    # Test case 3: person has only silver
    personCash = {'silver': 10}
    assert getPersonCashInGold(personCash) == 0.1

    # Test case 4: person has only gold
    personCash = {'gold': 1}
    assert getPersonCashInGold(personCash) == 1

    # Test case 5: person has only platinum
    personCash = {'platinum': 0.1}
    assert getPersonCashInGold(personCash) == 10

    # Test case 6: person has a mix of different types of cash
    personCash = {'copper': 100, 'silver': 10, 'gold': 1, 'platinum': 0.1}
    assert getPersonCashInGold(personCash) == 11.11

test_getPersonCashInGold()