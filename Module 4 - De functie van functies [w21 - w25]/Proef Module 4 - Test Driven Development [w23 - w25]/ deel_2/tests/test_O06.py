import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from data import friends
from functions import getFromListByKeyIs, getAdventuringPeople, getShareWithFriends, getAdventuringFriends

expected = 6
result = len(friends)
test('friends imported', expected, result)

testarg_list_alltests = [{
        'name' : 'Pie',
        'tasty' : True,
        'round' : True
    },{
        'name' : 'Fries',
        'tasty' : True,
        'round' : False
    },{
        'name' : 'Soccerball',
        'tasty' : False,
        'round' : True
    }]

expected = [{
        'name' : 'Pie',
        'tasty' : True,
        'round' : True
    },{
        'name' : 'Soccerball',
        'tasty' : False,
        'round' : True
    }]
result = getFromListByKeyIs(testarg_list_alltests, 'round', True)
test('getFromListByKeyIs - test 1',expected, result)


expected = [{
        'name' : 'Pie',
        'tasty' : True,
        'round' : True
    },{
        'name' : 'Soccerball',
        'tasty' : False,
        'round' : True
    }]
result = getFromListByKeyIs(testarg_list_alltests, 'round', True)
test('getFromListByKeyIs - test 2',expected, result)


expected = [{
        'name' : 'Pie',
        'tasty' : True,
        'round' : True
    },{
        'name' : 'Fries',
        'tasty' : True,
        'round' : False
    }]
result = getFromListByKeyIs(testarg_list_alltests, 'tasty', True)
test('getFromListByKeyIs - test 3',expected, result)


expected = [{
        'name' : 'Fries',
        'tasty' : True,
        'round' : False
    }]
result = getFromListByKeyIs(testarg_list_alltests, 'round', False)
test('getFromListByKeyIs - test 4',expected, result)


expected = []
result = getFromListByKeyIs(testarg_list_alltests, 'name', 'notExistingValue')
test('getFromListByKeyIs - test 5',expected, result)


expected = []
result = getFromListByKeyIs(testarg_list_alltests, 'notExistingKey', '?')
test('getFromListByKeyIs - test 6',expected, result)


expected = []
result = getAdventuringPeople([])
test('getAdventuringPeople - test 1',expected, result)

expected = [{'adventuring' : True}]
test2_people = [{'adventuring' : True}]
result = getAdventuringPeople(test2_people)
test('getAdventuringPeople - test 2',expected, result)

expected = []
test3_people = [{'adventuring' : False}]
result = getAdventuringPeople(test3_people)
test('getAdventuringPeople - test 3',expected, result)


expected = []
result = getShareWithFriends([])
test('getShareWithFriends - test 1',expected, result)

expected = [{'shareWith' : True}]
test2_people = [{'shareWith' : True}]
result = getShareWithFriends(test2_people)
test('getShareWithFriends - test 2',expected, result)

expected = []
test3_people = [{'shareWith' : False}]
result = getShareWithFriends(test3_people)
test('getShareWithFriends - test 3',expected, result)



expected = []
result = getAdventuringFriends([])
test('getAdventuringFriends - test 1',expected, result)

expected = [{'adventuring' : True, 'shareWith' : True}]
test2_people = [{'adventuring' : True, 'shareWith' : True}]
result = getAdventuringFriends(test2_people)
test('getAdventuringFriends - test 2', expected, result)

expected = []
test3_people = [{'adventuring' : False, 'shareWith' : True}]
result = getAdventuringFriends(test3_people)
test('getAdventuringFriends - test 3',expected, result)

expected = []
test4_people = [{'adventuring' : True, 'shareWith' : False}]
result = getAdventuringFriends(test4_people)
test('getAdventuringFriends - test 4',expected, result)

expected = []
test5_people = [{'adventuring' : False, 'shareWith' : False}]
result = getAdventuringFriends(test3_people)
test('getAdventuringFriends - test 5',expected, result)


if __name__ == "__main__":
    report()
