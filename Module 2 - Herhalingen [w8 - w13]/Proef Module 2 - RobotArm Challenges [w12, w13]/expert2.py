from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[2],0)

# your code starts here: 
robotArm.speed = 4
for i in range (9):
    robotArm.grab()
    robotArm.scan()
    if robotArm.scan() == "red":
        robotArm.moverightfunc(10 - i)
        robotArm.drop()
        robotArm.moveleftfunc(10 - i)
        
    else:
        robotArm.drop()
    robotArm.moveRight()
   



# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()