import sys, os
from test_lib import report, add_test_result

currentDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(currentDir))

dirItems = os.listdir(currentDir)
dirItems.sort()

for dirItem in dirItems:
    fullPath = currentDir + '/' + dirItem
    if os.path.isfile(fullPath) and dirItem[:5] == 'test_' and dirItem[-3:] == '.py' and dirItem != 'test_lib.py':
        try:
            add_test_result(vars=[f'\n======= [{dirItem}] =======\n'], color='magenta')
            __import__(dirItem[:-3])
        except Exception as e:
            add_test_result(txt = '{}: error when loading ' + dirItem, vars=['failed'], color='red')
            add_test_result(txt = '  exception: {} : {}', vars=[type(e).__name__, e])
            add_test_result(txt = '')

report()