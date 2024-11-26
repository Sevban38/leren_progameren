from challenges.solutions import *

challenges = {
    1 : {
        'start' : '4w', 
        'solution': ',4w', 
        'name': 'move stack to right', 
        'levels': '2:10,3:9/15', 
        'info':'move stack one spot to the right'
    },
    2 : {
        'start': ',6x', 
        'solution': hasSolution, 
        'criteria':'b:0,g:2', 
        'name': 'sort 6 boxes', 
        'symbols':'x-bbbbbggggg', 
        'levels':'2:16,3:18/30', 
        'info':'blue boxes to spot 0, green boxes to spot 2'
    },
    3 : {
        'start' : '5y', 
        'solution': ',,,,5y', 
        'name': 'move stack to spot 4', 
        'levels': '2:11,3:12/46', 
        'info':'move the whole stack to spot 4'
    },
    4 : {
        'name':'split stack in two colors','start' : ',rwrwrw', 
        'solution': 'www,,rrr',
        'levels':'2:14,3:15/24',
        'info':'move white boxes to spot 0 en red boxes to spot 2'
    },
    5 : {
        'name':'stack to end',
        'start' : ',7r', 
        'solution': ',,,,,,,,,7r',
        'levels':'2:13,3:13/119',
        'info': 'move all boxes of the stack to the last spot'
    }
}