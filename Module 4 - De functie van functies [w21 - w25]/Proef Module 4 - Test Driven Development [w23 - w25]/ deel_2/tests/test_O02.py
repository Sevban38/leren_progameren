import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from data import mainCharacter

expected = True
result = len(mainCharacter['name']) > 0
test('Character has a name',expected, result)

if __name__ == "__main__":
    report()