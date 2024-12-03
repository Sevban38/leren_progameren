from challenges.solutions import *

challenges = {
    1 : {
        'name':'move all stacks',
        'start' : 'b,2g,3w,4r', 
        'solution': ',,,,,b,2g,3w,4r',
        'levels':'2:15,3:15/112'
    },
    2 : {
        'name':'reds to the end',
        'start' : 'x,x,x,x,x,x,x,x,x,', 
        'symbols': 'x-rrrrwgbywgby', 
        'solution': hasSolution,
        'criteria':'r:9',
        'example':exampleSolution
    },
    3 : {
        'name':'stack distributed to the right',
        'start' : '???*?,,,,,,,,,',
        'solution': hasSolution, 
        'criteria':'0}1',
        'example':exampleSolution ,
        'levels':'2:25,3:17/63'
    },
    4 : {
        'name':'sort in stacks: rgb',
        'start' : 'x,x,x,x,x,x,,r,g,b', 
        'symbols':'x-rrrrbbbbgggg', 
        'solution': hasSolution,
        'criteria':'r:7,g:8,b:9',
        'example':exampleSolution
    },
    5 : {
        'name':'democratie',
        'start' : ',x,x,x,x,x,x,x,x,x', 
        'symbols':'x-rrrrryyyyybbbbb', 
        'solution': hasDemocratie, 
        'example':getDemocratieSolution,
        'levels':'2:35,3:35/110',
        'info':'collect all boxes of most common color on spot 0. If equally counted collect boxes of the first color found'
    }
}