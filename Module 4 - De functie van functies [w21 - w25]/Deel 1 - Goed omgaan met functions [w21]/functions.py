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