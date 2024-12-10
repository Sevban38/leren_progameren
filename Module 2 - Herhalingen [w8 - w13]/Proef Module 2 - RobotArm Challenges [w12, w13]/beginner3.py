from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.beginner import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[3],0)

# your code starts here:
def grabandgoback(whereto):
   robotArm.grab()
   robotArm.moverightfunc(whereto)
   robotArm.drop()
   robotArm.moveleftfunc(whereto)
grabandgoback(4)
grabandgoback(4)
grabandgoback(4)
grabandgoback(4)
grabandgoback(4)
grabandgoback(4)

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()