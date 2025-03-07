import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from functions import copper2silver, silver2gold, copper2gold, platinum2gold, getPersonCashInGold

expected = 1.0
result = copper2silver(10)
test('copper2silver - test 1',expected, result)

expected = 1.1
result = copper2silver(11)
test('copper2silver - test 2',expected, result)

expected = 2.0
result = silver2gold(10)
test('silver2gold - test 1',expected, result)

expected = 2.6
result = silver2gold(13)
test('silver2gold - test 2',expected, result)

expected = 0.2
result = copper2gold(10)
test('copper2gold - test 1',expected, result)

expected = 0.32
result = copper2gold(16)
test('copper2gold - test 2',expected, result)

expected = 25
result = platinum2gold(1)
test('platinum2gold - test 1',expected, result)

expected = 250
result = platinum2gold(10)
test('platinum2gold - test 2',expected, result)


testarg_personcash_test1 = {
    'platinum' : 1,
    'gold' : 1,
    'silver' : 1,
    'copper' : 1
}
expected = 26.22
result = getPersonCashInGold(testarg_personcash_test1)
test('getPersonCashInGold - test 1',expected, result)


testarg_personcash_test2 = {
    'platinum' : 22,
    'gold' : 38,
    'silver' : 12,
    'copper' : 3120
}
expected = 652.8
result = getPersonCashInGold(testarg_personcash_test2)
test('getPersonCashInGold - test 2',expected, result)


if __name__ == "__main__":
    report()