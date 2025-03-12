import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from functions import getJourneyFoodCostsInGold
from data import COST_FOOD_HUMAN_COPPER_PER_DAY, COST_FOOD_HORSE_COPPER_PER_DAY

expected = 4
result = COST_FOOD_HUMAN_COPPER_PER_DAY
test('COST_FOOD_HUMAN_COPPER_PER_DAY is correct', expected, result)

expected = 3
result = COST_FOOD_HORSE_COPPER_PER_DAY
test('COST_FOOD_HORSE_COPPER_PER_DAY is correct', expected, result)

expected = 1.54
result = getJourneyFoodCostsInGold(1,1)
test('getJourneyFoodCostsInGold - test 1',expected, result)

expected = 12.54
result = getJourneyFoodCostsInGold(12,3)
test('getJourneyFoodCostsInGold - test 2',expected, result)

expected = 28.38
result = getJourneyFoodCostsInGold(24,11)
test('getJourneyFoodCostsInGold - test 3',expected, result)

expected = 0.0
result = getJourneyFoodCostsInGold(0,0)
test('getJourneyFoodCostsInGold - test 4',expected, result)

expected = 15.4
result = getJourneyFoodCostsInGold(10,10)
test('getJourneyFoodCostsInGold - test 5',expected, result)


if __name__ == "__main__":
    report()
