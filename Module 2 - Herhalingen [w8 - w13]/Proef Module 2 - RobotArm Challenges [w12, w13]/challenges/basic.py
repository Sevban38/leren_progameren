from challenges.solutions import *

challenges =  {
    1 : {
        'start': ',,l', 
        'solution': 'l', 
        'name': 'box to start', 
        'levels':'2:10,3:10/6', 
        'info':'move box to spot 0'
    },
    2 : {
        'start': ',r,b', 
        'solution': ',b,r', 
        'name': 'swap boxes', 
        'levels': '2:18,3:18/14',
         'info':'swap de spots of the boxes'
    },
    3 : {
        'start': 'dy', 
        'solution': 'yd', 
        'name': 'swap boxes in stack', 
        'levels': '2:22,3:22/18', 
        'info':'swap de the boxes within the stack'
    },
    4 : {
        'start' : 'b,,,,b,,,b' , 
        'solution': ',,,,,,,,,bbb', 
        'name': 'collect boxes', 
        'levels':'2:20,3:20/29', 
        'info':'move all boxes to the last spot'
    },
    5 : {
        'start': ',x', 
        'solution': hasSolution, 
        'criteria':'r:0,y:2', 
        'name': 'sort 1 box', 
        'symbols':'x-ry', 'levels': 
        '2:12,3:11/5',
        'example':exampleSolution, 
        'info':'red to spot 0, yellow to spot 2'},
}