from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[1],0)

# your code starts here: 
robotArm.grab()
robotArm.moverightfunc(10)
robotArm.drop()
robotArm.moveleftfunc(9)
for i in range (2):
    robotArm.grab()
    robotArm.moverightfunc(8)
    robotArm.drop()
    robotArm.moveleftfunc(8)
robotArm.moveRight()
for i in range (3):
    robotArm.grab()
    robotArm.moverightfunc(6)
    robotArm.drop()
    robotArm.moveleftfunc(6)
robotArm.moveRight()
for i in range (4):
    robotArm.grab()
    robotArm.moverightfunc(4)
    robotArm.drop()
    robotArm.moveleftfunc(4)



# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()