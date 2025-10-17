from time import sleep

import robot

arlo = robot.Robot()

print ("Running ...")

lefspeed = 83
rightspeed = 80

# print(arlo.go_diff(lefspeed, rightspeed, 1, 1))  # Forward
# sleep(2)

# print(arlo.go_diff(lefspeed, rightspeed, 0, 1))  # Turn right
# sleep(0.6)


for i in range (5):
    print(arlo.drive_forward_meter(1, lefspeed, rightspeed))  # Forward
    print(arlo.rotate_robot(90))  # Turn right
    