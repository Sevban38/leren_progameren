from RobotArm import RobotArm

# Import the challenges (in this case challenges/example.py)
from challenges.expert import challenges

# load the robotarm with a challenge on a level (max 3)
robotArm = RobotArm(challenges[3],0)

# your code starts here: 
nummer = 1
for i in range (9):
    
    robotArm.grab()
    robotArm.moverightfunc(nummer)
    robotArm.drop()
    robotArm.moveleftfunc(nummer)
    nummer += 1
   



# your code ends here

# report the results of the mission
robotArm.report()

# want help? Unlock code below!
robotArm.help()

# want to inspect a solution? Unlock code below!
# robotArm.showSolution()
# robotArm.wait()