from math_operations import increment, decrement, add, subtract, multiply, divide
from test_lib import test, report

nr1 = 3.0
nr2 = 17.0

#de increment functie
expected = nr2 + 1
calculated = increment(nr2)
test('increment', expected, calculated)

#de decrement functie
expected = nr2 - 1
calculated = decrement(nr2)
test('decrement', expected, calculated)

#de add functie
expected = nr1 + nr2
calculated = add(nr1, nr2)
test('add', expected, calculated)

#de subtract functie
expected = nr2 - nr1
calculated = subtract(nr2, nr1)
test('subtract', expected, calculated)

#de multiply functie
expected = nr1 * nr2
calculated = multiply(nr1, nr2)
test('multiply', expected, calculated)

#de divide functie
expected = nr1 / nr2
calculated = divide(nr1, nr2)
test('divide', expected, calculated)

#deling door nul
expected = None
calculated = divide(nr1, 0)
test('divide by zero', expected, calculated)

# Genereer een rapport van alle tests
report()
