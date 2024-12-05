from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here: 
# Move the robot arm to the starting position
robotArm.speed=4
robotArm.grab()
robotArm.scan()
if robotArm.scan() == "red":
    robotArm.moverightfunc(8)
    robotArm.drop()
    robotArm.moveleftfunc(7)
elif robotArm.scan() == "green":
    robotArm.moverightfunc(9)
    robotArm.drop()
    robotArm.moveleftfunc(8)
else :
    robotArm.moverightfunc(10)
    robotArm.drop()
    robotArm.moveleftfunc(9)
robotArm.grab()
if robotArm.scan() == "red":
    robotArm.moverightfunc(7)
    robotArm.drop()
    robotArm.moveleftfunc(6)
elif robotArm.scan() == "green":
    robotArm.moverightfunc(8)
    robotArm.drop()
    robotArm.moveleftfunc(7)
else :
    robotArm.moverightfunc(9)
    robotArm.drop()
    robotArm.moveleftfunc(8)
robotArm.grab()
if robotArm.scan() == "red":
    robotArm.moverightfunc(6)
    robotArm.drop()
    robotArm.moveleftfunc(5)
elif robotArm.scan() == "green":
    robotArm.moverightfunc(7)
    robotArm.drop()
    robotArm.moveleftfunc(6)
else :
    robotArm.moverightfunc(8)
    robotArm.drop()
    robotArm.moveleftfunc(7)
robotArm.grab()
if robotArm.scan() == "red":
    robotArm.moverightfunc(5)
    robotArm.drop()
    robotArm.moveleftfunc(4)
elif robotArm.scan() == "green":
    robotArm.moverightfunc(6)
    robotArm.drop()
    robotArm.moveleftfunc(5)
else :
    robotArm.moverightfunc(7)
    robotArm.drop()
    robotArm.moveleftfunc(6)
robotArm.grab()
if robotArm.scan() == "red":
    robotArm.moverightfunc(4)
    robotArm.drop()
    robotArm.moveleftfunc(3)
elif robotArm.scan() == "green":
    robotArm.moverightfunc(5)
    robotArm.drop()
    robotArm.moveleftfunc(4)
else :
    robotArm.moverightfunc(6)
    robotArm.drop()
    robotArm.moveleftfunc(5)
robotArm.grab()
if robotArm.scan() == "red":
    robotArm.moverightfunc(3)
    robotArm.drop()
    robotArm.moveleftfunc(2)
elif robotArm.scan() == "green":
    robotArm.moverightfunc(4)
    robotArm.drop()
    robotArm.moveleftfunc(3)
else :
    robotArm.moverightfunc(5)
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