from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.basic import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:
robotArm.moverightfunc(5)
robotArm.grab()
robotArm.moveleftfunc(5)
robotArm.drop()
robotArm.moverightfunc(8)
robotArm.grab()
robotArm.moveleftfunc(8)
robotArm.drop()

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()