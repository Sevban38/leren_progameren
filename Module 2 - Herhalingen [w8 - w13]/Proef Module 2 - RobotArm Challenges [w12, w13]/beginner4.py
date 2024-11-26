from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.beginner import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here:
def grabandscan():
    robotArm.grab()
    kleur = robotArm.scan()
    if kleur == "red":
       robotArm.moveRight()
       robotArm.drop()
       robotArm.moveLeft()
    elif kleur == "white":
       robotArm.moveLeft()
       robotArm.drop()
       robotArm.moveRight()

robotArm.moveRight()
grabandscan()
grabandscan()  
grabandscan()
grabandscan()
grabandscan()
grabandscan()

# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()