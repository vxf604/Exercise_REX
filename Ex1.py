from time import sleep

import robot

arlo = robot.Robot()

print ("Running ...")

print(arlo.go_diff(80, 80, 1, 1))  # Forward
sleep(2)