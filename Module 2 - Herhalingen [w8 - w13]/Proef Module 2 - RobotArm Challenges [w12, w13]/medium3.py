from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[3],0)

# your code starts here: 
robotArm.moverightfunc(9)
def grabandcheckifwhite():
    robotArm.grab()
    if robotArm.scan() == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveleftfunc(3)
    else:
        robotArm.drop()
        robotArm.moveLeft()
        
for x in range (1, 10):
    grabandcheckifwhite()





# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()