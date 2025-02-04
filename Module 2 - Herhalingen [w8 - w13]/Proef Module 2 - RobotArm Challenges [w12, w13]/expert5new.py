from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[5],0)

# your code starts here: 
# Move the robot arm to the starting position
red = 0
yellow = 0
blue = 0
robotArm.speed = 4

color_dict = {
    "red": red,
    "yellow": yellow,
    "blue": blue
}

for i in range(10):
    robotArm.moveRight()
    robotArm.grab()
    color = robotArm.scan()
    robotArm.drop()
    
    if color in color_dict:
        color_dict[color] += 1

robotArm.moveleftfunc(10)
robotArm.moveRight()

for color, count in color_dict.items():
    if count == max(color_dict.values()):
        print(f"{color} >= {', '.join([c for c in color_dict if color_dict[c] == count])} = true")
        for i in range(11):
            robotArm.grab()
            scancolor = robotArm.scan()
            
            if scancolor == color:
                robotArm.moveleftfunc(2 + i)
                robotArm.drop()
                robotArm.moverightfunc(1 + i)
                returncount =+ 1
                if returncount == count:
                    quit()
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