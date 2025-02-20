from functions import *
from test_lib import *

number1 = 1
number2 = 1

Calculations_addittion = {
    'get_som' : lambda number1, number2: number1 + number2,
}
Calculations_multiply = {
    'get_som' : lambda number1, number2: number1 * number2,
}
Calculations_devide = {
    'get_som' : lambda number1, number2: number1 / number2,
}
Calculations_subtraction = {
    'get_som' : lambda number1, number2: number1 - number2,
}

expected = addition(number1, number2)
result = int(Calculations_addittion['get_som'](number1, number2))
test('TEST: addition(number1, number2)', expected, result)

expected = multiplication(number1, number2)
result = int(Calculations_multiply['get_som'](number1, number2))
test('TEST: addition(number1, number2)', expected, result)

expected = division(number1, number2)
result = float(Calculations_devide['get_som'](number1, number2))
test('TEST: addition(number1, number2)', expected, result)

expected = subtraction(number1, number2)
result = int(Calculations_subtraction['get_som'](number1, number2))
test('TEST: addition(number1, number2)', expected, result)


report()
