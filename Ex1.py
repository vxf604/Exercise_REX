from time import sleep

import robot

arlo = robot.Robot()

print ("Running ...")

lefspeed = 84
rightspeed = 80

print(arlo.go_diff(lefspeed, rightspeed, 1, 1))  # Forward
sleep(2)

print(arlo.go_diff(lefspeed, rightspeed, 0, 1))  # Turn right
sleep(0.75)