from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

# your code starts here: 
def grabdropandgoback():
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
def move1leftstack():
    grabdropandgoback()
    grabdropandgoback()
    grabdropandgoback()
    grabdropandgoback()
    grabdropandgoback()
    grabdropandgoback()

robotArm.moverightfunc(10)
def movestackandnextstack():  
    move1leftstack()
    robotArm.moveleftfunc(3)

for x in range (1, 5):
    movestackandnextstack()





# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()