from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.medium import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[1],0)

# your code starts here:
def move1right():
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveleftfunc(3)
robotArm.moverightfunc(9)
move1right()
move1right()
move1right()
move1right()
move1right()
move1right()
move1right()
move1right()
move1right()

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()