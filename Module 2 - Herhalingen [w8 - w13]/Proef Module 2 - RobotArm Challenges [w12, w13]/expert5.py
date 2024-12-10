from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here: 
# Move the robot arm to the starting position
red= 0
yellow = 0 
blue = 0
robotArm.speed=4
for i in range(10):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        robotArm.drop()
        red += 1 
    elif color == "yellow":
        robotArm.drop()
        yellow += 1
    elif color == "blue":
        robotArm.drop()
        blue += 1
    robotArm.moveRight()
robotArm.moveleftfunc(10)
if red >= blue and red >= yellow and blue >= yellow:
    print("red >= blue and red >= yellow and blue >= yellow = true")
    for i in range (10):
        robotArm.grab()
        color = robotArm.scan()
        if color == "red":
            robotArm.moveleftfunc(10 - i)
            robotArm.drop()
        elif color == "blue":
            robotArm.moveleftfunc(10 - i)
            robotArm.moveRight()
            robotArm.drop()
        elif color == "yellow":
            robotArm.moveleftfunc(10 - i)
            robotArm.moveRight()
            robotArm.moveRight()
            robotArm.drop()
        robotArm.moveRight()
elif red >= blue and red >= yellow and yellow > blue:
    print("red >= blue and red >= yellow and yellow > blue = true")
    for i in range (10):
        robotArm.grab()
        color = robotArm.scan()
        if color == "red":
            robotArm.moveleftfunc(10 - i)
            robotArm.drop()
        elif color == "yellow":
            robotArm.moveleftfunc(10 - i)
            robotArm.moveRight()
            robotArm.drop()
        elif color == "blue":
            robotArm.moveleftfunc(10 - i)
            robotArm.moveRight()
            robotArm.moveRight()
            robotArm.drop()
        robotArm.moveRight()
elif blue >= red and blue >= yellow and red >= yellow:
    print("blue >= red and blue >= yellow and red >= yellow = true")
    for i in range (10):
        robotArm.grab()
        color = robotArm.scan()
        if color == "blue":
            robotArm.moveleftfunc(10 - i)
            robotArm.drop()
        elif color == "red":
            robotArm.moveleftfunc(10 - i)
            robotArm.moveRight()
            robotArm.drop()
        elif color == "yellow":
            robotArm.moveleftfunc(10 - i)
            robotArm.moveRight()
            robotArm.moveRight()
            robotArm.drop()
        robotArm.moveRight()
elif blue >= red and blue >= yellow and yellow >= red:
    print(" blue >= red and blue >= yellow and yellow >= red = true")
    for i in range (10):
        robotArm.grab()
        color = robotArm.scan()
        if color == "blue":
            robotArm.moveleftfunc(10 - i)
            robotArm.drop()
        elif color == "yellow":
            robotArm.moveleftfunc(10 - i)
            robotArm.moveRight()
            robotArm.drop()
        elif color == "red":
            robotArm.moveleftfunc(10 - i)
            robotArm.moveRight()
            robotArm.moveRight()
            robotArm.drop()
        robotArm.moveRight()
elif yellow >= red and yellow >= blue and red >= blue:
    print("yellow >= red and yellow >= blue and red >= blue = true")
    for i in range (10):
        robotArm.grab()
        color = robotArm.scan()
        if color == "yellow":
            robotArm.moveleftfunc(10 - i)
            robotArm.drop()
        elif color == "red":
            robotArm.moveleftfunc(10 - i)
            robotArm.moveRight()
            robotArm.drop()
        elif color == "blue":
            robotArm.moveleftfunc(10 - i)
            robotArm.moveRight()
            robotArm.moveRight()
            robotArm.drop()
        robotArm.moveRight()
elif yellow >= red and yellow >= blue and blue >= red:
    print(" yellow >= red and yellow >= blue and blue >= red = true")
    for i in range (10):
        robotArm.grab()
        color = robotArm.scan()
        if color == "yellow":
            robotArm.moveleftfunc(10 - i)
            robotArm.drop()
        elif color == "blue":
            robotArm.moveleftfunc(10 - i)
            robotArm.moveRight()
            robotArm.drop()
        elif color == "red":
            robotArm.moveleftfunc(10 - i)
            robotArm.moveRight()
            robotArm.moveRight()
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