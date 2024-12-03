from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[4],0)

# your code starts here: 
# Move the robot arm to the starting position
robotArm.speed=4
red = 0
blue = 0
green = 0
for i in range(10):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        robotArm.drop()
        red =+ 1 
    elif color == "green":
        robotArm.drop()
        green =+ 1
    elif color == "blue":
        robotArm.drop()
        blue =+ 1
    robotArm.moveRight()
robotArm.moveleftfunc(10)
if red > blue and red > green and blue > green:
    for i in range (10):
        robotArm.grab()
        color = robotArm.scan()
        if color == "red":
            robotArm.moveleftfunc(10)
            robotArm.drop()
        elif color == "blue":
            robotArm.moveleftfunc(10)
            robotArm.moveRight()
            robotArm.drop()
        elif color == "green":
            robotArm.moveleftfunc(10)
            robotArm.moveRight()
            robotArm.moveRight()
            robotArm.drop()
        robotArm.moveRight()
elif red > blue and red > green and green > blue:
    for i in range (10):
        robotArm.grab()
        color = robotArm.scan()
        if color == "red":
            robotArm.moveleftfunc(10)
            robotArm.drop()
        elif color == "green":
            robotArm.moveleftfunc(10)
            robotArm.moveRight()
            robotArm.drop()
        elif color == "blue":
            robotArm.moveleftfunc(10)
            robotArm.moveRight()
            robotArm.moveRight()
            robotArm.drop()
        robotArm.moveRight()
elif blue > red and blue > green and red > green:
    for i in range (10):
        robotArm.grab()
        color = robotArm.scan()
        if color == "blue":
            robotArm.moveleftfunc(10)
            robotArm.drop()
        elif color == "red":
            robotArm.moveleftfunc(10)
            robotArm.moveRight()
            robotArm.drop()
        elif color == "green":
            robotArm.moveleftfunc(10)
            robotArm.moveRight()
            robotArm.moveRight()
            robotArm.drop()
        robotArm.moveRight()
elif blue > red and blue > green and green > red:
    for i in range (10):
        robotArm.grab()
        color = robotArm.scan()
        if color == "blue":
            robotArm.moveleftfunc(10)
            robotArm.drop()
        elif color == "green":
            robotArm.moveleftfunc(10)
            robotArm.moveRight()
            robotArm.drop()
        elif color == "red":
            robotArm.moveleftfunc(10)
            robotArm.moveRight()
            robotArm.moveRight()
            robotArm.drop()
        robotArm.moveRight()
elif green > red and green > blue and red > blue:
    for i in range (10):
        robotArm.grab()
        color = robotArm.scan()
        if color == "green":
            robotArm.moveleftfunc(10)
            robotArm.drop()
        elif color == "red":
            robotArm.moveleftfunc(10)
            robotArm.moveRight()
            robotArm.drop()
        elif color == "blue":
            robotArm.moveleftfunc(10)
            robotArm.moveRight()
            robotArm.moveRight()
            robotArm.drop()
        robotArm.moveRight()
elif green > red and green > blue and blue > red:
    for i in range (10):
        robotArm.grab()
        color = robotArm.scan()
        if color == "green":
            robotArm.moveleftfunc(10)
            robotArm.drop()
        elif color == "blue":
            robotArm.moveleftfunc(10)
            robotArm.moveRight()
            robotArm.drop()
        elif color == "red":
            robotArm.moveleftfunc(10)
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