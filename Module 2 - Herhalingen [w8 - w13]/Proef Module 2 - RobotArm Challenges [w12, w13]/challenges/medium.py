from challenges.solutions import *

challenges = {
    1 : {
        'name':'move all boxes to right',
        'start' : 'r,b,w,g,g,b,r,w,y', 
        'solution': ',r,b,w,g,g,b,r,w,y',
        'levels':'2:13,3:13/51',
        'info':'move all boxes one spot to the right'
    },
    2 : {
        'name':'move all stacks to left',
        'start' : ',6b,,6b,,6b,,6b,,6b', 
        'solution': '6b,,6b,,6b,,6b,,6b',
        'levels':'2:13,3:14/128',
        'info':'move all stacks one spot to the left'
    },
    3 : {
        'name':'whites to the right',
        'start' : 'x,x,x,x,x,x,x,x,x,', 
        'symbols': 'x-wwwwwwrgbrgbrgb', 
        'solution': hasSolution,
        'criteria':'w>1',
        'example':exampleSolution,
        'scans':'5:9',
        'levels':'2:17,3:17/55',
        'info':'move all white boxes one spot to the right'
    },
    4 : {
        'name':'move stack exactly to right',
        'start' : 'bwgrw', 
        'solution': ',bwgrw',
        'levels':'2:18,3:20/43',
        'info':'move the stack one space to the right, with all the boxes in the same order'
    },
    5 : {
        'name':'flip all boxes over',
        'start' : 'g,b,w,r,b', 
        'solution': ',,,,,b,r,w,b,g',
        'levels':'2:17,3:11/55',
        'info':'Use robotArm.showSolution() to display desired solution'
    }
}