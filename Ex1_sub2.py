from time import sleep

import robot

arlo = robot.Robot()

print ("Running ...")


lefspeed = 43
rightspeed = 90
i = 3
while i < 3: 
    print(arlo.go_diff(lefspeed, rightspeed, 1, 1))  # Forward
    sleep(6.85)
    print(arlo.go_diff(rightspeed, lefspeed, 1, 1))  # Forward
    sleep(8)
    i += 1