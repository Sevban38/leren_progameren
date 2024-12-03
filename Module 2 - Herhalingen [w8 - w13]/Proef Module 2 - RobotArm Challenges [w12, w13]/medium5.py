from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here: 
robotArm.grab()
robotArm.moverightfunc(10)
robotArm.drop()
robotArm.moveleftfunc(9)
robotArm.grab()
robotArm.moverightfunc(8)
robotArm.drop()
robotArm.moveleftfunc(7)
robotArm.grab()
robotArm.moverightfunc(6)
robotArm.drop()
robotArm.moveleftfunc(5)
robotArm.grab()
robotArm.moverightfunc(4)
robotArm.drop()
robotArm.moveleftfunc(3)
robotArm.grab()
robotArm.moverightfunc(2)
robotArm.drop()



# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()