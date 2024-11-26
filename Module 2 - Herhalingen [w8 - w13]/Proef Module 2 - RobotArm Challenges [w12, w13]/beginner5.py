from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.beginner import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here:
def grabandgoback(whereto):
   robotArm.grab()
   robotArm.moverightfunc(whereto)
   robotArm.drop()
   robotArm.moveleftfunc(whereto)
robotArm.moverightfunc(2)
grabandgoback(9)
grabandgoback(9)
grabandgoback(9)
grabandgoback(9)
grabandgoback(9)
grabandgoback(9)
grabandgoback(9)


# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()