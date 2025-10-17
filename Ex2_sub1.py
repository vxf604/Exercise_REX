from time import sleep

import robot

arlo = robot.Robot()

print ("Running ...")

for i in range (5):
    if arlo.read_front_ping_sensor() < 20:
        arlo.rotate_robot(90)
        print(arlo.go_diff(80, 80, 1, 1))  # Forward
    elif arlo.read_left_ping_sensor() < 20:
        arlo.rotate_robot(-90)
        print(arlo.go_diff(80, 80, 1, 1))  # Forward
    elif arlo.read_right_ping_sensor() < 20:
        arlo.rotate_robot(90)
        print(arlo.go_diff(80, 80, 1, 1))  # Forward
    else:
        print(arlo.go_diff(80, 80, 1, 1))  # Forward
        
print ("Finished")