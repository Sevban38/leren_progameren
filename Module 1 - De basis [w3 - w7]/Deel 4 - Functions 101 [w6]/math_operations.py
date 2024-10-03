# math_operations.py

# Increment function is al klaar
def increment(nr: float) -> float:
    return nr + 1

# Decrement function (vermindert met 1)
def decrement(nr: float) -> float:
    return nr - 1

# Add function (optellen van twee getallen)
def add(nr1: float, nr2: float) -> float:
    return nr1 + nr2

# Subtract function (aftrekken van twee getallen)
def subtract(nr1: float, nr2: float) -> float:
    return nr1 - nr2

# Multiply function (vermenigvuldigen van twee getallen)
def multiply(nr1: float, nr2: float) -> float:
    return nr1 * nr2

# Divide function (deling van twee getallen met uitzondering voor deling door nul)
def divide(nr1: float, nr2: float) -> float:
    try:
        return nr1 / nr2
    except ZeroDivisionError:
        return None  # Als nr2 0 is, return None
