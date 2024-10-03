#import hier je functie "from [bestandsnaamZonderExtentie] import [functieNaam]"
from test_lib2 import test, report

if __name__ == "__main__":
    report()
    def compare_numbers(nr1, nr2):
        if nr1 == nr2:
            return "equal"
        elif nr1 > nr2:
            return "greater"
        else:
            return "less"

    # Test cases
    expected = 'equal'
    result = compare_numbers(5, 5)
    test('TEST nr1=nr2', expected, result)

    expected = 'greater'
    result = compare_numbers(10, 5)
    test('TEST nr1>nr2', expected, result)

    expected = 'less'
    result = compare_numbers(3, 5)
    test('TEST nr1<nr2', expected, result)

    if __name__ == "__main__":
        report()