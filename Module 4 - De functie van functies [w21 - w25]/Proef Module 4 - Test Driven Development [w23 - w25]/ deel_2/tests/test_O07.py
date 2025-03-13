import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from functions import getNumberOfHorsesNeeded, getNumberOfTentsNeeded, getTotalRentalCost
from data import COST_TENT_GOLD_PER_WEEK, COST_HORSE_SILVER_PER_DAY

expected = 3
result = COST_TENT_GOLD_PER_WEEK
test('COST_TENT_GOLD_PER_WEEK is correct', expected, result)

expected = 5
result = COST_HORSE_SILVER_PER_DAY
test('COST_HORSE_SILVER_PER_DAY is correct', expected, result)

expected = 4
result = getNumberOfHorsesNeeded(7)
test('getNumberOfHorsesNeeded - test 1',expected, result)

expected = 2
result = getNumberOfHorsesNeeded(4)
test('getNumberOfHorsesNeeded - test 2',expected, result)

expected = 3
result = getNumberOfTentsNeeded(7)
test('getNumberOfTentsNeeded - test 1',expected, result)

expected = 3
result = getNumberOfTentsNeeded(8)
test('getNumberOfTentsNeeded - test 2',expected, result)

expected = 2
result = getNumberOfTentsNeeded(6)
test('getNumberOfTentsNeeded - test 3',expected, result)

expected = 23.0
result = getTotalRentalCost(1,2)
test('getTotalRentalCost - test 1',expected, result)

expected = 67.0
result = getTotalRentalCost(5,2)
test('getTotalRentalCost - test 2',expected, result)

expected = 99.0
result = getTotalRentalCost(3,11)
test('getTotalRentalCost - test 3',expected, result)

if __name__ == "__main__":
    report()