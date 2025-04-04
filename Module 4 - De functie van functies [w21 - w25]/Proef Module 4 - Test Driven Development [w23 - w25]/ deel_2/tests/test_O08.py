import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from data import adventurerGear
from functions import getItemsAsText, getItemsValueInGold

expected = 9
result = len(adventurerGear)
test('gear imported', expected, result)

testarg_items_test1 = [{
    'name' : 'Kaars',
    'amount' : 3,
    'unit' : 'x',
    'price' : {
        'amount' : 4,
        'type' : 'copper'
    }
}]

expected = '3x Kaars'
result = getItemsAsText(testarg_items_test1)
test('getItemsAsText - test 1',expected, result)

expected = 0.24
result = getItemsValueInGold(testarg_items_test1)
test('getItemsValueInGold - test 1',expected, result)

testarg_items_test2 = [{
    'name' : 'Diamand',
    'amount' : 1,
    'unit' : '',
    'price' : {
        'amount' : 7,
        'type' : 'platinum'
    }
}]
expected = '1 Diamand'
result = getItemsAsText(testarg_items_test2)
test('getItemsAsText - test 2',expected, result)

expected = 175.0
result = getItemsValueInGold(testarg_items_test2)
test('getItemsValueInGold - test 2',expected, result)


testarg_items_test3 = [{
    'name' : 'Appelsap',
    'amount' : 5,
    'unit' : 'l',
    'price' : {
        'amount' : 1,
        'type' : 'gold'
    }
},{
    'name' : 'Een pannekoek',
    'amount' : 10,
    'unit' : 'x',
    'price' : {
        'amount' : 0.5,
        'type' : 'gold'
    }
}]
expected = '5l Appelsap & 10x Een pannekoek'
result = getItemsAsText(testarg_items_test3)
test('getItemsAsText - test 3',expected, result)

expected = 10.0
result = getItemsValueInGold(testarg_items_test3)
test('getItemsValueInGold - test 3',expected, result)

testarg_items_test4 = [{
    'name' : 'Voetbal',
    'amount' : 1,
    'unit' : ' ronde',
    'price' : {
        'amount' : 2,
        'type' : 'gold'
    }
},{
    'name' : 'Patat',
    'amount' : 11,
    'unit' : 'x',
    'price' : {
        'amount' : 4,
        'type' : 'silver'
    }
},{
    'name' : 'Cola',
    'amount' : 1,
    'unit' : 'l',
    'price' : {
        'amount' : 5,
        'type' : 'copper'
    }
},{
    'name' : 'Sinas',
    'amount' : 5,
    'unit' : 'dl',
    'price' : {
        'amount' : 12,
        'type' : 'copper'
    }
}]
expected = '1 ronde Voetbal, 11x Patat, 1l Cola & 5dl Sinas'
result = getItemsAsText(testarg_items_test4)
test('getItemsAsText - test 4',expected, result)

expected = 12.1
result = getItemsValueInGold(testarg_items_test4)
test('getItemsValueInGold - test 4',expected, result)


if __name__ == "__main__":
    report()