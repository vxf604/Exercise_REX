from time import sleep

import robot

arlo = robot.Robot()

print ("Running ...")


lefspeed = 83
rightspeed = 50
print(arlo.go_diff(lefspeed, rightspeed, 1, 1))  # Forward
sleep(7)